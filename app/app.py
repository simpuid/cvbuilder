from flask import *
from werkzeug.urls import url_parse
from flask_bootstrap import Bootstrap

from db import *
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from config import AppConfig
from forms import LoginForm, PasswordForm, StudentForm
from tables import *

app = Flask(__name__)
app.config.from_object(AppConfig)
login = LoginManager(app)
Bootstrap(app)
login.login_view = 'login'

initialize('cv_data', 'init.sql')
populate_users()


@login.user_loader
def load_user(uid):
    return User.load(int(uid))


@app.route('/')
@login_required
def home():
    student = Student.load(current_user.id)
    if student is not None:
        name = student.name
    else:
        name = current_user.id
    return render_template('home.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.load(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/password', methods=['GET', 'POST'])
@login_required
def password():
    form = PasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.current_password.data):
            flash('Current Password wrong', 'danger')
            return redirect(url_for('password'))
        current_user.set_password(form.new_password.data)
        current_user.save()
        commit()
        logout_user()
        return redirect(url_for('login'))
    return render_template('password.html', form=form)


@app.route('/student', methods=['GET', 'POST'])
@login_required
def edit_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(current_user.id, form.name.data, form.phone.data, form.email.data, form.dob.data,
                          form.branch.data,
                          form.minor.data, form.year.data)
        student.save()
        commit()
        flash('Data updated successfully', 'success')
        return redirect(url_for('edit_student'))
    student = Student.load(current_user.id)
    form.name.data, form.phone.data, form.email.data = student.name, student.phone, student.email
    form.dob.data, form.branch.data, form.minor.data, = student.dob, student.branch, student.minor
    form.year.data = student.year
    return render_template('student.html', form=form)


@app.route('/sharam')
def handle_sharam():
    return render_template('sharam.html'), 403


@app.errorhandler(404)
def handle_404(e):
    return render_template("404_error.html"), 404
