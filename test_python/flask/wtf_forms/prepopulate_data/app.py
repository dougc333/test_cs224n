from ast import Pass
from tokenize import String
from flask import Flask, render_template
from flask_wtf import FlaskForm
from pytest import PytestAssertRewriteWarning
from wtforms import StringField, IntegerField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Email

from dataclasses import dataclass

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(), 
        Length(min=3, max=7, message="length more than 3 less than 7")
    ])    
    password = PasswordField('Password', validators=[
        InputRequired(),
        AnyOf(values="password")
    ])
    age = IntegerField("age", default=100)
    yesno = BooleanField("yesno")
    email = StringField('email')

class DataClassForm(FlaskForm):
    user = StringField('UserName',validators=[
        InputRequired()
    ])
    gender = BooleanField('M/F', validators=[
        InputRequired()
    ])

class User:
    def __init__(self, username, age, email):
        self.username=username
        self.age = age
        self.email = email

#try replacing with dataclass
@dataclass
class UserDataClass:
    name: str = "default username"
    gender: str = "M"

    


def create_app():
    app = Flask(__name__)
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SECRET_KEY']= 'asdfasdfasdf'
    
    #we have to add the routes in here 
    @app.route("/", methods=['GET','POST'])
    def login():
        user = User(username="bob", age=100, email="foo@foo.com")
        form = LoginForm(obj=user)
        if form.validate_on_submit():
            return f"<h1>Username:{form.username.data} Password:{form.password.data}"
        
        return render_template('index.html', form=form)

    @app.route("/dataclass", methods=['GET','POST'])
    def test():
        form_dataclass = DataClassForm(obj=UserDataClass())
        if form_dataclass.validate_on_submit():
            return "/dataclass route login form with user dataclass object not valid "
        return render_template("index_dataclass.html",form=form_dataclass)
    return app