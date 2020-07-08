from wtforms import Form, BooleanField, StringField, PasswordField, validators
from app.models import User

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Email("Invalid email address")])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(Form):
    email = StringField('Email Address', [validators.Email("Invalid email address")])
    password = PasswordField('Password', [validators.DataRequired("Password field required")])





