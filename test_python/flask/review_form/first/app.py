from flask import render_template, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.secret_key = b'_53oi3uriq9pifpff;apl'


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")


@app.route('/', methods=['GET'])
def index():
    '''
    default index.html page
    '''
    form = LoginForm()
    return render_template('index.html', form=form)
