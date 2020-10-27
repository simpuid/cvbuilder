from flask_login import login_required, current_user
from flask import Blueprint, redirect, url_for, make_response, flash
from models import Resume

blueprint = Blueprint('download', __name__)


@blueprint.route('/download')
@login_required
def download():
    resume = Resume.load(current_user.id)
    if resume is not None:
        response = make_response(resume.data)
        response.headers.set('Content-Type', 'application/pdf')
        response.headers.set('Content-Disposition', 'attachment', filename='resume.pdf')
        return response
    flash('No generated resume found', 'danger')
    return redirect(url_for('dashboard.dashboard'))
