from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length,AnyOf, Email

#flaskform includes CRSF, wtforms doesnt
class LoginForm(FlaskForm):
    username = StringField('username', validators=[
        InputRequired(),
        Length(min=3, max=8)
    ])
    password1 = PasswordField('password', validators=[
        InputRequired(),
        AnyOf(values=["foo"])
    ])
    #how to make both passwords the same?
    password2 = PasswordField('password', validators=[
        InputRequired(),
        AnyOf(values=["foo"])
    ])
    age = IntegerField('age', validators=[
        InputRequired(),
    ])
    gender = BooleanField("M/F", validators=[
        InputRequired(),
    ])
    email=StringField("email:",validators=[
        Email(),
    ])

#if we dont put index inside then we have to use blueprints 
def create_app():   
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secrettoken"
    @app.route("/", methods = ['GET','POST'])
    def index():
        form = LoginForm()
        print("form.data:",form.data)
        print("form username errors:",form.username.errors)
        #print("dir:",dir(form))
        if form.validate_on_submit():
            return f"<h1>Username:{form.username.data} Password:{form.password.data} \
            Age:{form.age.data} Gender:{form.gender.data} \
            Email:{form.email.data}</h1>"
        
        form.username.label="foo" #the default is username. this should be easier to find in the docs
        return render_template('index.html',form=form)
    return app

