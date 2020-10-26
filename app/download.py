from flask import send_file
from flask import render_template, Blueprint
from flask_login import current_user, login_required
from models import *

blueprint = Blueprint('file-downloads', __name__)

@blueprint.route('/file-downloads')
@login_required
def file_download():
    try:
        return render_template('download.html')
    except Exception as e:
        return str(e)

@blueprint.route('/return-files/')
@login_required
def return_file(): 
    filename = './' + str(current_user.id) + '.md'
    try:
        return send_file(filename , attachment_filename='Resume.md')
    except Exception as e:
        return str(e)
