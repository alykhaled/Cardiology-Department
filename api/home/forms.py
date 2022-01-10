from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired
from wtforms import StringField, validators, PasswordField, SubmitField, TextAreaField

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class ContactForm(FlaskForm):
  email = StringField("Email",  [validators.DataRequired()])
  subject = StringField("Subject",  [validators.DataRequired(),validators.Email()])
  message = TextAreaField("Message",  [validators.DataRequired()])
  submit = SubmitField("Send")