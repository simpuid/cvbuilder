from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList, FormField, Form


class ReferenceForm(Form):
    professor_email = StringField('Professor\'s Email')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class ReferenceListForm(FlaskForm):
    ref_list = FieldList(FormField(ReferenceForm))
    professor_email = StringField('Professor\'s Email')
    add = SubmitField('Add')
