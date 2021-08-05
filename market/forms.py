from re import S
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForms(FlaskForm):
    username = StringField(label='')
    email_address = StringField(label='')
    pass1 = PasswordField(label='')
    pass2 = PasswordField(label='' )
    submit = SubmitField(label='Create Account')