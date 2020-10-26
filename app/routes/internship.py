from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for

from forms import InternshipListForm
from models import Internship
from db import commit

blueprint = Blueprint('internship', __name__)


@blueprint.route('/internship', methods=['GET', 'POST'])
@login_required
def internship():
    Entry = namedtuple('Entry', ['organization', 'designation', 'start', 'end', 'text_description'])
    intern_value = Internship.load(current_user.id)
    if intern_value.intern_list:
        data = {'intern_list': []}
        for intern_dict in intern_value.intern_list:
            data['intern_list'].append(
                Entry(intern_dict['organization'], intern_dict['designation'], intern_dict['start_date'],
                      intern_dict['end_date'],
                      intern_dict['description']))
        form = InternshipListForm(data=data)
    else:
        form = InternshipListForm()
    if form.validate_on_submit():
        if form.add.data:
            if bool(form.organization.data) and bool(form.designation.data) and bool(form.start.data) and bool(
                    form.end.data):
                intern_dict = {
                    'organization': form.organization.data,
                    'designation': form.designation.data,
                    'start_date': form.start.data,
                    'end_date': form.end.data,
                    'description': form.text_description.data
                }
                intern_value.add(intern_dict)
                flash('Internship added', 'success')
                commit()
            else:
                flash('Empty field', 'danger')
            return redirect(url_for('internship.internship'))
        else:
            for index in range(len(form.intern_list)):
                if form.intern_list[index].save.data:
                    if bool(form.intern_list[index].organization.data) and bool(
                            form.intern_list[index].designation.data) and bool(
                            form.intern_list[index].start.data) and bool(
                            form.intern_list[index].end.data):
                        intern_dict = {
                            'organization': form.intern_list[index].organization.data,
                            'designation': form.intern_list[index].designation.data,
                            'start_date': form.intern_list[index].start.data,
                            'end_date': form.intern_list[index].end.data,
                            'description': form.intern_list[index].text_description.data
                        }
                        intern_value.update(index, intern_dict)
                        commit()
                        flash('Updated successfully', 'success')
                    else:
                        flash('Empty field', 'danger')
                    return redirect(url_for('internship.internship'))
                if form.intern_list[index].delete.data:
                    intern_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('internship.internship'))
    return render_template('internship.html', form=form)
