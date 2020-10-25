from models import Student
from flask_login import login_required, current_user
from flask import render_template, Blueprint

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
@login_required
def home():
    student = Student.load(current_user.id)
    if student is not None:
        name = student.name
    else:
        name = current_user.id
    return render_template('home.html', name=name)
