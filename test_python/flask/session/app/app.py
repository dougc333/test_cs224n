from flask import Flask, render_template, session, redirect, url_for
#session acts like dictionary

app = Flask(__name__)
app.config['SECRET_KEY'] ="asdfase33243"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/set-background/<mode>')
def set_background(mode):
    session['mode'] = mode
    return redirect(url_for('index'))

@app.route('drop-session')
def drop_session():
    session.pop('mode',None)
    return redirect(url_for('index'))