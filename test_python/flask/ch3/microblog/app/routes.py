
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

loggedin_user = {"username":'bob'}

posts = [
    {
    "author":{"username":"first user"},
    "body": "first post"
    },
    {
    "author":{"username":"second user"},
    "body": "second post"        
    },
    {
    "author":{"username":"third user"},
    "body": "third post"
    }

]

#this isnt really correct we should do a redirect
@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index2")
def index2():
    return render_template('index2.html',title = "Index Page")

@app.route('/login',methods=['GET','POST'])
def login():
    print("login form")
    form = LoginForm()
    if form.validate_on_submit():
        print("validate on submit login",form.username.data, form.remember_me.data)
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    #cafeful logged_in user requires session. 
    return render_template('login.html',title='Sign In', form=form, loggedin_user=loggedin_user)

@app.route('/loops')
def l():
    return render_template("index2.html",title="Display all posts", posts=posts, loggedin_user=loggedin_user)
