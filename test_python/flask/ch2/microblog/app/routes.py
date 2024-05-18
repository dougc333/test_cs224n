from app import app
from flask import render_template

user={"username":"ann"}
posts=[
  {'author':{'username':"bob"},
   'body':'first post'},
  {'author':{'username':"ann"},
   'body':'second post'},
  {'author':{'username':"ccc"},
   'body':'third post'},
  {'author':{'username':"ddd"},
   'body':'fourth post'}
]

@app.route("/index")
def index_template():
  return render_template('index.html', title="Template", user=user)

@app.route("/notitle")
def anyname():
  return render_template('conditional.html',user=user)

@app.route("/title")
def have_title():
  return render_template('conditional.html', title="Conditional Jinja",user=user)


@app.route('/loops')
def test_loops():
  return render_template('loop.html',posts=posts)

@app.route('/index2')
def i2():
  return render_template('index2.html', posts=posts, user=user)

@app.route('/')
def index():
  return '''
   <html>
   <head>
   <title>ch2 templates title</title>
   </head>
   <body>
   <p>'''+user["username"]+'''</p>
   </body>
   </html>
	 '''


