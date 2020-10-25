from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, DateField
from wtforms.validators import DataRequired, Email, NumberRange


class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired(message='It should be a number')])
    email = StringField('Email ID', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth', validators=[DataRequired(message='Supported format: YYYY-MM-DD')])
    branch = StringField('Branch', validators=[DataRequired()])
    minor = StringField('Minor', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1, max=4, message='Invalid Year')])
    submit = SubmitField('Submit')
