from flask import *
from werkzeug.urls import url_parse

from db import *
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from config import AppConfig
from forms import LoginForm, PasswordForm
from model import User, populate_users

app = Flask(__name__)
app.config.from_object(AppConfig)
login = LoginManager(app)
login.login_view = 'login'

initialize('cv_data', 'init.sql')
populate_users()


@login.user_loader
def load_user(uid):
    return User.load(int(uid))


@app.route('/')
@login_required
def home():
    return render_template('home.html', title='Welcome')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.load(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)


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
            flash('Current Password wrong')
            return redirect(url_for('password'))
        current_user.set_password(form.new_password.data)
        current_user.apply()
        commit()
        logout_user()
        return redirect(url_for('home'))
    return render_template('password.html', title='Change Password', form=form)
