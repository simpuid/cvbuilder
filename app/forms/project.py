from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList, FormField, Form, DateField, TextAreaField
from wtforms.validators import Optional


class ProjectForm(Form):
    title = StringField('Title')
    professors = TextAreaField('Professors\'s Email')
    start = DateField('Start Date', validators=[Optional()])
    end = DateField('End Date', validators=[Optional()])
    text_description = TextAreaField('Description')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class ProjectListForm(FlaskForm):
    project_list = FieldList(FormField(ProjectForm))
    title = StringField('Title')
    professors = TextAreaField('Professors\'s Email')
    start = DateField('Start Date', validators=[Optional()])
    end = DateField('End Date', validators=[Optional()])
    text_description = TextAreaField('Description')
    add = SubmitField('Add')
