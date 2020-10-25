from flask_wtf import FlaskForm
from wtforms import SubmitField, FieldList, FormField, Form, TextAreaField


class AchievementForm(Form):
    achievement_description = TextAreaField('Achievement')
    save = SubmitField('Save')
    delete = SubmitField('Delete')


class AchievementListForm(FlaskForm):
    achievement_list = FieldList(FormField(AchievementForm))
    new_achievement = TextAreaField('Achievement')
    add = SubmitField('Add')
