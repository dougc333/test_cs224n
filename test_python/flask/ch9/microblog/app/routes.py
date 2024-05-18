from app import app, db
from app.forms import LoginForm, RegistrationForm, EmptyForm, EditProfileForm
from app.forms import PostForm
from app.models import User, Post
from flask_login import current_user, logout_user, login_user, login_required
from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from datetime import datetime



@app.before_request
def before_request():
  '''
  add time to each visit
  '''
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow()
    print("commit to db")
    db.session.commit()


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    """
    default index page
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash("post now live")
        return redirect(url_for("index"))
    page = request.args.get('page',1, type=int)
    print("index routes current_user:",current_user)
    posts = current_user.followed_posts().paginate(
    page=page, per_page = app.config['POSTS_PER_PAGE'],error_out= False)
    next_url = url_for('explore', page = posts.next_num) if posts.has_next else None
    prev_url = url_for('explore',page = post.prev_num) if posts.has_prev else None
    return render_template('index.html', title="Explore",form=form, posts=posts.items, next_url = next_url, prev_url=prev_url)


@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
      page=page, per_page = app.config['POSTS_PER_PAGE'],error_out = False)
    print("explore route posts:",posts)
    next_url = url_for('explore', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('explore',page=posts.prev_num) if posts.has_prev else None
    print('routes.py explore post: %s' % posts)
    return render_template('index.html', title="Explore", posts=posts, next_url = next_url, prev_url=prev_url)


@app.route('/login',methods=['GET','POST'])
def login():
  '''
    login
  '''
  print("Login")
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
      if not next_page or url_parse(next_page).netloc !='':
          next_page = url_for('index')
      return redirect(next_page)
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

@app.route('/user/<username>', methods=['GET'])
@login_required
def user(username):
  """user login"""
  print("User login username:", username)
  user = User.query.filter_by(username=username).first_or_404()
  posts = [
  {'author': user, 'body': 'Test post #1'},
  {'author': user, 'body': 'Test post #2'}
  ]
  form = EmptyForm()
  return render_template('user.html', user=user, posts=posts,form=form)


@app.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    '''edit profile'''
    form = EditProfileForm(current_user.username)
    print("creted edirprofile form")
    if form.validate_on_submit():
        print("edit profile validate on submit")
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("changes saved")
        return redirect(url_for('edit_profile'))
    elif request.method=='GET':
       
        form.username.data = current_user.username  
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',title="Edit Profile",form=form)

@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))

@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))