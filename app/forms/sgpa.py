from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FieldList, FormField, Form, FloatField
from wtforms.validators import NumberRange, Optional


class SGPAForm(Form):
    semester = IntegerField('Semester', validators=[Optional()])
    sgpa = FloatField('SGPA', validators=[Optional()])
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class CGPAForm(FlaskForm):
    sg_list = FieldList(FormField(SGPAForm))
    semester = IntegerField('Semester', validators=[Optional()])
    sgpa = FloatField('SGPA', validators=[Optional()])
    add = SubmitField('Add')
