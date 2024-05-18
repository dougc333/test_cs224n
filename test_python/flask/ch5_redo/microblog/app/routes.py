from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, logout_user, login_user, login_required
from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse




user={'username': 'bob'}
posts=[
  {
    "author":{'username': 'author1'},
    "title":'title1',
    "body": 'body1'
  },
  {
    "author":{'username': 'author2'},
    "title":'title2',
    "body": 'body2'      
  },
  {
    "author":{'username': 'author3'},
    "title":'title3',
    "body": 'body3'
  }
]

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title="Home", posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
	"""
	login docstring
	"""
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	print("form: " + str(form.__dict__))
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first() 
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or passsword')
			return redirect(url_for('login'))
		login_user(user,remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(url_for('index'))
	return render_template('login.html',title="Login Form", form=form)

		

@app.route('/logout')
def logout():
    """
    logout. Verify what happends to current_user
    """
    print('logout current_user before logging out',current_user)
    logout_user()
    print('logout current_user after logging out',current_user)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data,email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("Registration successful")
		return redirect(url_for('login'))
	return render_template('register.html', title="Registration", form=form)
