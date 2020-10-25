from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for
from forms import AchievementListForm
from models import Achievement
from db import commit

blueprint = Blueprint('achievement', __name__)


@blueprint.route('/achievement', methods=['GET', 'POST'])
@login_required
def achievement():
    Entry = namedtuple('Entry', ['achievement_description'])
    achievement_value = Achievement.load(current_user.id)
    if achievement_value.achievement_list:
        data = {'achievement_list': []}
        for achievement_description in achievement_value.achievement_list:
            data['achievement_list'].append(Entry(achievement_description))
        form = AchievementListForm(data=data)
    else:
        form = AchievementListForm()
    if form.validate_on_submit():
        if form.add.data:
            if bool(form.new_achievement.data):
                achievement_value.add(form.new_achievement.data)
                flash('Achievement added', 'success')
                commit()
            else:
                flash('Empty achievement', 'danger')
            return redirect(url_for('achievement.achievement'))
        else:
            for index in range(len(form.achievement_list)):
                if form.achievement_list[index].save.data:
                    if bool(form.achievement_list[index].achievement_description.data):
                        achievement_value.update(index, form.achievement_list[index].achievement_description.data)
                        commit()
                        flash('Updated successfully', 'success')
                    else:
                        flash('Empty achievement', 'danger')
                    return redirect(url_for('achievement.achievement'))
                if form.achievement_list[index].delete.data:
                    achievement_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('achievement.achievement'))
    return render_template('achievement.html', form=form)
