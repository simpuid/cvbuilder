from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, IntegerField, StringField, DateField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(FlaskForm):
    username = IntegerField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')


class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    branch = StringField('Branch', validators=[DataRequired()])
    minor = StringField('Minor', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
