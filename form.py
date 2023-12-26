from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, EqualTo, Email

class SignUpForm(FlaskForm):
    firstname =  StringField("Name", validators=[length(min=1, max=20, message="Name is too short")])
    lastname = StringField("Last Name", validators=[length(min=3, max=25, message="Lastname is too short")])
    email = StringField("Email")
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Sign Up")
    accept_tos = BooleanField('I accept the Terms of Use & Privacy Policy', validators=[DataRequired()])
    

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(message="name is too short")])
    password = PasswordField("Password", validators=[DataRequired(), length(min=8, max=16, message="name is too short")])
    submit = SubmitField("Login")
    