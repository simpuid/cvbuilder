from flask_login import login_required, current_user
from flask import Blueprint, redirect, url_for
from models import Resume
from db import commit
from generator import render_latex

import subprocess
import os

blueprint = Blueprint('generate', __name__)


@blueprint.route('/generate')
@login_required
def generate():
    content = render_latex(current_user.id)
    xtx = f'/output/{current_user.id}.xtx'
    pdf = f'/output/{current_user.id}.pdf'
    with open(xtx, 'w') as file:
        file.write(content)
    subprocess.check_call(['xelatex', '-output-directory=/output/', xtx], cwd='/app/generator/')
    with open(pdf, 'rb') as file:
        data = file.read()
    resume = Resume(current_user.id, data)
    resume.save()
    commit()
    junk = [xtx, pdf, f'/output/{current_user.id}.aux', f'/output/{current_user.id}.log',
            f'/output/{current_user.id}.out', ]
    for path in junk:
        if os.path.isfile(path):
            os.remove(path)
    return redirect(url_for('dashboard.dashboard'))
