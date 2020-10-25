from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, IntegerField, StringField, DateField, FloatField, Form, FieldList, \
    FormField
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange
import datetime


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
    phone = IntegerField('Phone', validators=[DataRequired(message='It should be a number')])
    email = StringField('Email ID', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth', validators=[DataRequired(message='Supported format: YYYY-MM-DD')])
    branch = StringField('Branch', validators=[DataRequired()])
    minor = StringField('Minor', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1, max=4, message='Invalid Year')])
    submit = SubmitField('Submit')


class TenthForm(FlaskForm):
    school_name = StringField('School Name', validators=[DataRequired()])
    cgpa = FloatField('CGPA', validators=[DataRequired(), NumberRange(min=0, max=10, message='On a scale of 10')])
    board = StringField('Board', validators=[DataRequired()])
    year = IntegerField('Year',
                        validators=[DataRequired(), NumberRange(min=1947, max=(datetime.datetime.now().year - 2),
                                                                message='Invalid Year')])
    submit = SubmitField('Submit')


class TwelfthForm(FlaskForm):
    school_name = StringField('School Name', validators=[DataRequired()])
    cgpa = FloatField('CGPA', validators=[DataRequired(), NumberRange(min=0, max=10, message='On a scale of 10')])
    board = StringField('Board', validators=[DataRequired()])
    year = IntegerField('Year',
                        validators=[DataRequired(), NumberRange(min=1947, max=datetime.datetime.now().year,
                                                                message='Invalid Year')])
    submit = SubmitField('Submit')


class SkillForm(Form):
    skill_name = StringField('Skill')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class SkillListForm(FlaskForm):
    skill_list = FieldList(FormField(SkillForm))
    new_skill = StringField('Skill')
    add = SubmitField('Add')
