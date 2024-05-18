"""
A simple proxy server, based on original by gear11:
https://gist.github.com/gear11/8006132
Modified from original to support both GET and POST, status code passthrough, header and form data passthrough.
Usage: http://hostname:port/p/(URL to be proxied, minus protocol)
For example: http://localhost:5000/p/www.google.com
"""
import re
from urllib.parse import urlparse, urlunparse
from flask import Flask, request, abort, Response, redirect
import requests
import logging

app = Flask(__name__.split('.')[0])
logging.basicConfig(level=logging.INFO)
APPROVED_HOSTS = set(["localhost:4000", "www.google.com", "yahoo.com"])
CHUNK_SIZE = 1024
LOG = logging.getLogger("app.py")


@app.route('/<path:url>', methods=["GET", "POST"])
def root(url):
    # If referred from a proxy request, then redirect to a URL with the proxy prefix.
    # This allows server-relative and protocol-relative URLs to work.
    referer = request.headers.get('referer')
    if not referer:
        return Response("Relative URL sent without a a proxying request referal. Please specify a valid proxy host (/p/url)", 400)
    proxy_ref = proxied_request_info(referer)
    host = proxy_ref[0]
    print("root referer:",referer)
    print("root proxy_ref:",proxy_ref)
    print("root host:",host)
    print("root request.query_string:",request.query_string)
    print("root url:",url)
    redirect_url = "/p/%s/%s%s" % (host, url, ("?" + request.query_string.decode('utf-8') if request.query_string else ""))
    print("root redirect_url:", redirect_url)
    return redirect(redirect_url)


@app.route('/p/<path:url>', methods=["GET", "POST"])
def proxy(url):
    """Fetches the specified URL and streams it out to the client.
    If the request was referred by the proxy itself (e.g. this is an image fetch
    for a previously proxied HTML page), then the original Referer is passed."""
    # Check if url to proxy has host only, and redirect with trailing slash
    # (path component) to avoid breakage for downstream apps attempting base
    # path detection
    url_parts = urlparse('%s://%s' % (request.scheme, url))
    
    print("proxy url:",url)
    print("url_parts:",url_parts)
    if url_parts.path == "":
        parts = urlparse(request.url)
        LOG.warning("Proxy request without a path was sent, redirecting assuming '/': %s -> %s/" % (url, url))
        return redirect(urlunparse(parts._replace(path=parts.path+'/')))

    print("request.methpod: %s,  url: %s, request.headers: %s", request.method, url, request.headers)
    print("calling make_request")
    r = make_request(url, request.method, dict(request.headers), request.form)
    print("+++++r:",r)
    print("Got %s response from %s",r.status_code, url)
    headers = dict(r.raw.headers)
    print("headers:",headers)
    def generate():
        for chunk in r.raw.stream(decode_content=False):
            yield chunk
    out = Response(generate(), headers=headers)
    out.status_code = r.status_code
    print("out:",out)
    return out


def make_request(url, method, headers={}, data=None):
    print("make_request url:",url)
    print("make_request method:",method)
    print("make_request headers:",headers)
    url = 'http://%s' % url
    print("make_request url:",url)
    # Ensure the URL is approved, else abort
    if not is_approved(url):
        print("URL is not approved: %s", url)
        abort(403)
    print("approved")
    # Pass original Referer for subsequent resource requests
    referer = request.headers.get('referer')
    print("referer-------",referer)
    if referer:
        proxy_ref = proxied_request_info(referer)
        headers.update({ "referer" : "http://%s/%s" % (proxy_ref[0], proxy_ref[1])})

    # Fetch the URL, and stream it back
    print("make_request method:%s, url:%s  headers: %s, data: %s", method, url, headers, data)
    #result =  requests.request(method, url, params=request.args, stream=True, headers=headers, allow_redirects=False, data=data)
    result =  requests.request('GET', 'localhost:4000')
    print("####### make_request result:",result)
    return result
def is_approved(url):
    """Indicates whether the given URL is allowed to be fetched.  This
    prevents the server from becoming an open proxy"""
    parts = urlparse(url)

    b = parts.netloc in APPROVED_HOSTS
    print("parts:",parts," b:",b)
    return b
def proxied_request_info(proxy_url):
    """Returns information about the target (proxied) URL given a URL sent to
    the proxy itself. For example, if given:
        http://localhost:5000/p/google.com/search?q=foo
    then the result is:
        ("google.com", "search?q=foo")"""
    parts = urlparse(proxy_url)
    if not parts.path:
        return None
    elif not parts.path.startswith('/p/'):
        return None
    matches = re.match('^/p/([^/]+)/?(.*)', parts.path)
    proxied_host = matches.group(1)
    proxied_path = matches.group(2) or '/'
    proxied_tail = urlunparse(parts._replace(scheme="", netloc="", path=proxied_path))
    LOG.debug("Referred by proxy host, uri: %s, %s", proxied_host, proxied_tail)
    return [proxied_host, proxied_tail]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)