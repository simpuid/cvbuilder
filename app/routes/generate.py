from flask_login import login_required, current_user
from flask import Blueprint, redirect, url_for
from models import Resume
from db import commit

blueprint = Blueprint('generate', __name__)


def read_file(path: str):
    with open(path, 'rb') as file:
        data = file.read()
    return data


@blueprint.route('/generate')
@login_required
def generate():
    resume = Resume(current_user.id, read_file('sample.pdf'))
    resume.save()
    commit()
    return redirect(url_for('home.home'))
