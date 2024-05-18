from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm

user = {"username":"user1"}
posts = [
        {
          'author': {'username': 'John'},
          'body': 'Beautiful day in Portland!'
        },
        {
          'author': {'username': 'Susan'},
          'body': 'The Avengers movie was so cool!'
        }
    ]

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",title="Home",user=user, posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('login requested for user:{}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index')) 
	return render_template("login.html", title="Login",form=form)




