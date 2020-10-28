from flask_login import login_required, current_user
from flask import Blueprint, redirect, make_response, flash
from models import Resume

blueprint = Blueprint('resume', __name__)


@blueprint.route('/resume')
@login_required
def resume():
    res = Resume.load(current_user.id)
    if res is not None:
        response = make_response(res.data)
        response.headers.set('Content-Type', 'application/pdf')
        return response
    flash('No generated resume found', 'danger')
    return redirect('/static/images/not-found.png')
