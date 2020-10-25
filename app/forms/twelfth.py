from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, FloatField
from wtforms.validators import DataRequired, NumberRange
import datetime


class TwelfthForm(FlaskForm):
    school_name = StringField('School Name', validators=[DataRequired()])
    cgpa = FloatField('CGPA', validators=[DataRequired(), NumberRange(min=0, max=10, message='On a scale of 10')])
    board = StringField('Board', validators=[DataRequired()])
    year = IntegerField('Year',
                        validators=[DataRequired(), NumberRange(min=1947, max=datetime.datetime.now().year,
                                                                message='Invalid Year')])
    submit = SubmitField('Submit')
