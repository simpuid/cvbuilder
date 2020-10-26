from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList, FormField, Form, DateField, TextAreaField
from wtforms.validators import Optional


class InternshipForm(Form):
    organization = StringField('Organization')
    designation = StringField('Designation')
    start = DateField('Start Date', validators=[Optional()])
    end = DateField('End Date', validators=[Optional()])
    text_description = TextAreaField('Description')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class InternshipListForm(FlaskForm):
    intern_list = FieldList(FormField(InternshipForm))
    organization = StringField('Organization')
    designation = StringField('Designation')
    start = DateField('Start Date', validators=[Optional()])
    end = DateField('End Date', validators=[Optional()])
    text_description = TextAreaField('Description')
    add = SubmitField('Add')
