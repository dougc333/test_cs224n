from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError, Length
from flask_babel import _, lazy_gettext as _l

from app.models import User

class LoginForm(FlaskForm):
  '''
  Form for login
  '''
  username = StringField(_l('Username'), validators=[DataRequired()])
  password = PasswordField(_l('Password'), validators=[DataRequired()])
  remember_me = BooleanField(_l("Remember Me"))
  submit = SubmitField(_l('Submit'))


class RegistrationForm(FlaskForm):
  """
  Register user
  """
  username = StringField(_l('Username'), validators=[DataRequired()])
  email = StringField(_l('email'), validators=[DataRequired(),Email()])
  password = PasswordField(_l('Password'), validators=[DataRequired()])
  password2 = PasswordField(_l('Password2'), validators=[DataRequired(), EqualTo('password')])
  remember_me = BooleanField(_l("Remember Me"))
  submit = SubmitField(_l('Register'))

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError(_l('duplicate username'))

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError(_l('duplicate email'))
    
class EditProfileForm(FlaskForm):
  username = StringField(_l('Username'), validators = [DataRequired()])
  about_me = TextAreaField(_l('About Me'), validators=[Length(min=0,max=100)]) 
  submit = SubmitField(_l('Submit'))

  def __init__(self, original_username, *args, **kwargs):
    super(EditProfileForm, self).__init__(*args, **kwargs)
    self.original_username = original_username
  
  def validate_username(self, username):
    if username.data != self.original_username:
      user = User.query.filter_by(username = self.username.data).first()
      if user is not None:
        raise ValidationError(_l('username already taken'))
  

class EmptyForm(FlaskForm):
  submit = SubmitField(_l('Submit'))


class PostForm(FlaskForm):
  post = TextAreaField(_l('Post'), validators = [DataRequired(), Length(min=1, max=1000)])
  submit = SubmitField(_l('Submit'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))



