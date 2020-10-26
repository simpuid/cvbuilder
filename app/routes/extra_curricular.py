from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for

from forms import ECListForm
from models import ExtraCurricular
from db import commit

blueprint = Blueprint('extra_curricular', __name__)


@blueprint.route('/extra_curricular', methods=['GET', 'POST'])
@login_required
def extra_curricular():
    Entry = namedtuple('Entry', ['title', 'start', 'end', 'text_description'])
    ec_value = ExtraCurricular.load(current_user.id)
    if ec_value.ec_list:
        data = {'ec_list': []}
        for ec_dict in ec_value.ec_list:
            data['ec_list'].append(
                Entry(ec_dict['title'], ec_dict['start'], ec_dict['end'],
                      ec_dict['text_description']))
        form = ECListForm(data=data)
    else:
        form = ECListForm()
    if form.validate_on_submit():
        if form.add.data:
            if bool(form.title.data) and bool(form.start.data) and bool(form.end.data):
                ec_dict = {
                    'title': form.title.data,
                    'start': form.start.data,
                    'end': form.end.data,
                    'text_description': form.text_description.data
                }
                ec_value.add(ec_dict)
                flash('Extra-curricular activity added', 'success')
                commit()
            else:
                flash('Empty field', 'danger')
            return redirect(url_for('extra_curricular.extra_curricular'))
        else:
            for index in range(len(form.ec_list)):
                if form.ec_list[index].save.data:
                    if bool(form.ec_list[index].title.data) and bool(form.ec_list[index].start.data) and bool(
                            form.ec_list[index].end.data):
                        ec_dict = {
                            'title': form.ec_list[index].title.data,
                            'start': form.ec_list[index].start.data,
                            'end': form.ec_list[index].end.data,
                            'text_description': form.ec_list[index].text_description.data
                        }
                        ec_value.update(index, ec_dict)
                        commit()
                        flash('Updated successfully', 'success')
                    else:
                        flash('Empty field', 'danger')
                    return redirect(url_for('extra_curricular.extra_curricular'))
                if form.ec_list[index].delete.data:
                    ec_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('extra_curricular.extra_curricular'))
    return render_template('extra_curricular.html', form=form)
