from flask import Blueprint, redirect, url_for, flash, request, render_template
from flask_login import current_user, login_user
from models import User
from forms import LoginForm
from werkzeug.urls import url_parse

blueprint = Blueprint('login', __name__)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.load(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home.home')
        return redirect(next_page)
    return render_template('login.html', form=form)