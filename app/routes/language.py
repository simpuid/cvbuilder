from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for

from forms import LanguageListForm
from models import Language
from db import commit

blueprint = Blueprint('language', __name__)


@blueprint.route('/language', methods=['GET', 'POST'])
@login_required
def language():
    Entry = namedtuple('Entry', ['language_name', 'speaking', 'reading', 'writing'])
    language_value = Language.load(current_user.id)
    if language_value.language_list:
        data = {'language_list': []}
        for language_dict in language_value.language_list:
            data['language_list'].append(
                Entry(language_dict['language_name'], language_dict['speaking'], language_dict['reading'],
                      language_dict['writing']))
        form = LanguageListForm(data=data)
    else:
        form = LanguageListForm()
    if form.validate_on_submit():
        if form.add.data:
            if bool(form.new_language.data) and (form.speaking.data or form.reading.data or form.writing.data):
                language_dict = {
                    'language_name': form.new_language.data,
                    'speaking': form.speaking.data,
                    'reading': form.reading.data,
                    'writing': form.writing.data
                }
                language_value.add(language_dict)
                flash('Language added', 'success')
                commit()
            else:
                flash('Empty language field', 'danger')
            return redirect(url_for('language.language'))
        else:
            for index in range(len(form.language_list)):
                if form.language_list[index].save.data:
                    if bool(form.language_list[index].language_name.data) and (
                            form.language_list[index].speaking.data or form.language_list[index].reading.data or
                            form.language_list[index].writing.data):
                        language_dict = {
                            'language_name': form.language_list[index].language_name.data,
                            'speaking': form.language_list[index].speaking.data,
                            'reading': form.language_list[index].reading.data,
                            'writing': form.language_list[index].writing.data
                        }
                        language_value.update(index, language_dict)
                        commit()
                        flash('Updated successfully', 'success')
                    else:
                        flash('Empty language field', 'danger')
                    return redirect(url_for('language.language'))
                if form.language_list[index].delete.data:
                    language_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('language.language'))
    return render_template('language.html', form=form)
