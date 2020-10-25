from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for
from forms import SkillListForm
from models import Skill
from db import commit

blueprint = Blueprint('skill', __name__)


@blueprint.route('/skill', methods=['GET', 'POST'])
@login_required
def skill():
    Entry = namedtuple('Entry', ['skill_name'])
    skill_value = Skill.load(current_user.id)
    if skill_value.skill_list:
        data = {'skill_list': []}
        for skill_name in skill_value.skill_list:
            data['skill_list'].append(Entry(skill_name))
        form = SkillListForm(data=data)
    else:
        form = SkillListForm()
    if form.validate_on_submit():
        if form.add.data:
            if bool(form.new_skill.data):
                skill_value.add(form.new_skill.data)
                commit()
            else:
                flash('Empty skill', 'danger')
            return redirect(url_for('skill.skill'))
        else:
            for index in range(len(form.skill_list)):
                if form.skill_list[index].save.data:
                    if bool(form.skill_list[index].skill_name.data):
                        skill_value.update(index, form.skill_list[index].skill_name.data)
                        commit()
                        flash('Updated successfully', 'success')
                    else:
                        flash('Empty skill', 'danger')
                    return redirect(url_for('skill.skill'))
                if form.skill_list[index].delete.data:
                    skill_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('skill.skill'))
    return render_template('skill.html', form=form)
