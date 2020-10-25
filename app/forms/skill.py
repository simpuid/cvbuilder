from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList, FormField, Form


class SkillForm(Form):
    skill_name = StringField('Skill')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class SkillListForm(FlaskForm):
    skill_list = FieldList(FormField(SkillForm))
    new_skill = StringField('Skill')
    add = SubmitField('Add')
