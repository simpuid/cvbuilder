from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for
from forms import CGPAForm
from models import SGPA
from db import commit

blueprint = Blueprint('sgpa', __name__)


@blueprint.route('/sgpa', methods=['GET', 'POST'])
@login_required
def sgpa():
    Entry = namedtuple('Entry', ['semester', 'sgpa'])
    sgpa_value = SGPA.load(current_user.id)
    if sgpa_value.sg_list:
        data = {'sg_list': []}
        for sgpa_dict in sgpa_value.sg_list:
            data['sg_list'].append(Entry(sgpa_dict['semester'], sgpa_dict['value']))
        form = CGPAForm(data=data)
    else:
        form = CGPAForm()
    if form.validate_on_submit():
        if form.add.data:
            if form.semester.data and form.sgpa.data is not None and 1 <= form.semester.data <= 8 and \
                    0 <= form.sgpa.data <= 10:
                sgpa_dict = {
                    'semester': form.semester.data,
                    'value': form.sgpa.data,
                }
                sgpa_value.add(sgpa_dict)
                flash('SGPA added', 'success')
                commit()
            else:
                flash('Invalid values', 'danger')
            return redirect(url_for('sgpa.sgpa'))
        else:
            for index in range(len(form.sg_list)):
                if form.sg_list[index].save.data:
                    if form.sg_list[index].semester.data and form.sg_list[index].sgpa.data is not None and 1 <= \
                            form.sg_list[index].semester.data <= 8 and 0 <= form.sg_list[index].sgpa.data <= 10:
                        sgpa_dict = {
                            'semester': form.sg_list[index].semester.data,
                            'value': form.sg_list[index].sgpa.data,
                        }
                        sgpa_value.update(index, sgpa_dict)
                        commit()
                        flash('Updated successfully', 'success')
                    else:
                        flash('Invalid values', 'danger')
                    return redirect(url_for('sgpa.sgpa'))
                if form.sg_list[index].delete.data:
                    sgpa_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('sgpa.sgpa'))
    return render_template('sgpa.html', form=form)
