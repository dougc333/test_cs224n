from app import app,db
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm, RegisterationForm
from app.models import User
from flask_login import login_required, current_user, login_user, logout_user

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
@login_required
def index():
	return render_template("index.html",title="Home", posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password.')
			return redirect(url_for('login'))
		login_user(user,remember=form.remember_me.data)
		return redirect(url_for('index')) 
	return render_template("login.html", title="Login",form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route("/register", methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegisterationForm()
	if form.validate_on_submit():
		user= User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("Congratulations uyou are now a registered user")
		return redirect(url_for('login'))
	return render_template('register.html', title="Regsiter", form=form)
  
	  
