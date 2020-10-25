from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for
from forms import TenthForm
from models import Tenth
from db import commit

blueprint = Blueprint('tenth', __name__)


@blueprint.route('/tenth', methods=['GET', 'POST'])
@login_required
def tenth():
    form = TenthForm()
    if form.validate_on_submit():
        Tenth(current_user.id, form.school_name.data, form.cgpa.data, form.board.data, form.year.data).save()
        commit()
        flash('Data updated successfully', 'success')
        return redirect(url_for('tenth.tenth'))
    tenth_value = Tenth.load(current_user.id)
    if tenth_value is not None:
        form.school_name.data = tenth_value.school_name
        form.cgpa.data = tenth_value.cgpa
        form.board.data = tenth_value.board
        form.year.data = tenth_value.year
    return render_template('tenth.html', form=form)
