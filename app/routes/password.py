from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import login_required, current_user, logout_user
from forms import PasswordForm
from db import commit

blueprint = Blueprint('password', __name__)


@blueprint.route('/password', methods=['GET', 'POST'])
@login_required
def password():
    form = PasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.current_password.data):
            flash('Current Password wrong', 'danger')
            return redirect(url_for('password.password'))
        current_user.set_password(form.new_password.data)
        current_user.save()
        commit()
        logout_user()
        return redirect(url_for('login.login'))
    return render_template('password.html', form=form)
