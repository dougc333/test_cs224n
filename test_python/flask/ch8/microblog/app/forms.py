#from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError, Length
from app.models import User

class LoginForm(FlaskForm):
  '''
  Form for login
  '''
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField("Remember Me")
  submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
  """
  Register user
  """
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('email', validators=[DataRequired(),Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Password2', validators=[DataRequired(), EqualTo('password')])
  remember_me = BooleanField("Remember Me")
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('duplicate username')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('duplicate email')
    
class EditProfileForm(FlaskForm):
  username = StringField('Username', validators = [DataRequired()])
  about_me = TextAreaField('About Me', validators=[Length(min=0,max=100)]) 
  submit = SubmitField('Submit')

  def __init__(self, original_username, *args, **kwargs):
    super(EditProfileForm, self).__init__(*args, **kwargs)
    self.original_username = original_username
  
  def validate_username(self, username):
    if username.data != self.original_username:
      user = User.query.filter_by(username = self.username.data).first()
      if user is not None:
        raise ValidationError('username already taken')
  

class EmptyForm(FlaskForm):
  submit = SubmitField('Submit')
