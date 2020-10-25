from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for
from forms import TwelfthForm
from models import Twelfth
from db import commit

blueprint = Blueprint('twelfth', __name__)


@blueprint.route('/twelfth', methods=['GET', 'POST'])
@login_required
def twelfth():
    form = TwelfthForm()
    if form.validate_on_submit():
        Twelfth(current_user.id, form.school_name.data, form.cgpa.data, form.board.data, form.year.data).save()
        commit()
        flash('Data updated successfully', 'success')
        return redirect(url_for('twelfth.twelfth'))
    twelfth_value = Twelfth.load(current_user.id)
    if twelfth_value is not None:
        form.school_name.data = twelfth_value.school_name
        form.cgpa.data = twelfth_value.cgpa
        form.board.data = twelfth_value.board
        form.year.data = twelfth_value.year
    return render_template('twelfth.html', form=form)
