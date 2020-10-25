from flask import Blueprint, redirect, url_for, flash
from flask_login import logout_user

blueprint = Blueprint('logout', __name__)


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out', 'success')
    return redirect(url_for('home.home'))
