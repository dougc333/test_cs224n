from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

# can use create_app or make_app. most use create_app
# flask run automatically looks for app.py


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Mysecret!'

    @app.route('/')
    def index():
        form = LoginForm()
        return render_template('index.html', form=form)

    return app
