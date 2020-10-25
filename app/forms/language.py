from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList, FormField, Form, BooleanField


class LanguageForm(Form):
    language_name = StringField('Language')
    speaking = BooleanField('Speak')
    reading = BooleanField('Read')
    writing = BooleanField('Write')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class LanguageListForm(FlaskForm):
    language_list = FieldList(FormField(LanguageForm))
    new_language = StringField('Language')
    speaking = BooleanField('Speak')
    reading = BooleanField('Read')
    writing = BooleanField('Write')
    add = SubmitField('Add')
