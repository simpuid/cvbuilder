from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList, FormField, Form, DateField, TextAreaField
from wtforms.validators import Optional


class ECForm(Form):
    title = StringField('Title')
    start = DateField('Start Date', validators=[Optional()])
    end = DateField('End Date', validators=[Optional()])
    text_description = TextAreaField('Description')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class ECListForm(FlaskForm):
    ec_list = FieldList(FormField(ECForm))
    title = StringField('Title')
    start = DateField('Start Date', validators=[Optional()])
    end = DateField('End Date', validators=[Optional()])
    text_description = TextAreaField('Description')
    add = SubmitField('Add')
