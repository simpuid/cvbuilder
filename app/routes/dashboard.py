from models import Resume
from flask_login import login_required, current_user
from flask import render_template, Blueprint
import base64

blueprint = Blueprint('dashboard', __name__)


@blueprint.route('/dashboard')
@login_required
def dashboard():
    resume = Resume.load(current_user.id)
    download_disabled = True
    if resume is not None:
        download_disabled = False
    return render_template('dashboard.html', download_disabled=download_disabled)
