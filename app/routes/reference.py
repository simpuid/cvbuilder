from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for
from forms import ReferenceListForm
from models import Reference, Professor
from db import commit

blueprint = Blueprint('reference', __name__)


@blueprint.route('/reference', methods=['GET', 'POST'])
@login_required
def reference():
    Entry = namedtuple('Entry', ['professor_email'])
    ref_value = Reference.load(current_user.id)
    if ref_value.ref_list:
        data = {'ref_list': []}
        for professor_email in ref_value.ref_list:
            data['ref_list'].append(Entry(professor_email))
        form = ReferenceListForm(data=data)
    else:
        form = ReferenceListForm()
    if form.validate_on_submit():
        if form.add.data:
            if bool(form.professor_email.data) and Professor.load(form.professor_email.data) is not None:
                ref_value.add(form.professor_email.data)
                flash('Reference added', 'success')
                commit()
            else:
                flash('Invalid email', 'danger')
            return redirect(url_for('reference.reference'))
        else:
            for index in range(len(form.ref_list)):
                if form.ref_list[index].save.data:
                    if bool(form.ref_list[index].professor_email.data) and Professor.load(
                            form.ref_list[index].professor_email.data) is not None:
                        ref_value.update(index, form.ref_list[index].professor_email.data)
                        commit()
                        flash('Updated successfully', 'success')
                    else:
                        flash('Invalid email', 'danger')
                    return redirect(url_for('reference.reference'))
                if form.ref_list[index].delete.data:
                    ref_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('reference.reference'))
    return render_template('reference.html', form=form)
