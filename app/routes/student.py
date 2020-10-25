from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from forms import StudentForm
from tables import Student
from db import commit

blueprint = Blueprint('student', __name__)


@blueprint.route('/student', methods=['GET', 'POST'])
@login_required
def student():
    form = StudentForm()
    if form.validate_on_submit():
        Student(current_user.id, form.name.data, form.phone.data, form.email.data, form.dob.data,
                form.branch.data,
                form.minor.data, form.year.data).save()
        commit()
        flash('Data updated successfully', 'success')
        return redirect(url_for('student.student'))
    student_value = Student.load(current_user.id)
    if student_value is not None:
        form.name.data = student_value.name
        form.phone.data = student_value.phone
        form.email.data = student_value.email
        form.dob.data = student_value.dob
        form.branch.data = student_value.branch
        form.minor.data = student_value.minor
        form.year.data = student_value.year
    return render_template('student.html', form=form)
