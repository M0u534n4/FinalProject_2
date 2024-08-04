from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from wtforms.fields import StringField, IntegerField, SubmitField
# from wtforms.validators import InputRequired, DataRequired
# from wtforms.fields import MultipleFileField


# class SignUpForm(FlaskForm):
#     name = StringField("პროგრამის სახელი", validators=[InputRequired()])
#     price = StringField("დონე", validators=[InputRequired()])
#     img = FileField("სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "svg"])])
#     submit = SubmitField("დამატება")


# class AddPostForm(FlaskForm):
#     name = StringField("აღწერა", validators=[InputRequired()])
#     img = MultipleFileField("სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "svg"])])
#     submit = SubmitField("დამატება")



# class FileUpload(FlaskForm):
#     name = StringField("აღწერა", validators=[InputRequired()])
#     file = FileField('ფაილი', validators=[DataRequired(), FileAllowed(['pdf'], 'Only PDF files allowed!')])
#     submit = SubmitField('ატვირთვა')