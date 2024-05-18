from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

loggedin_user = {"username":"bob"}

posts=[
  {
  "author":{"username":"author1"},
  "title": "title1",
  "body":"body1"
  },
  {
  "author":{"username":"author2"},
  "title": "title2",
  "body":"body2"
  },
  {
  "author":{"username":"author3"},
  "title": "title3",
  "body":"body3"
  },
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=posts,loggedin_user=loggedin_user)

@app.route('/login')
def login():
    form = LoginForm()
    #process submit request
    if form.validate_on_submit():
      flash('login required for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
      return redirect('/index')
    return render_template('login.html',title="Login",form=form,loggedin_user=loggedin_user)




