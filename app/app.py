from flask import *
from werkzeug.urls import url_parse
from flask_bootstrap import Bootstrap

from db import *
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from config import AppConfig
from forms import LoginForm, PasswordForm, StudentForm
from tables import *
from routes import home, login, static, logout, password, student

initialize('cv_data', 'init.sql')
populate_users()

app = Flask(__name__)
app.config.from_object(AppConfig)
Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login.login'


@login_manager.user_loader
def load_user(uid):
    return User.load(int(uid))


app.register_blueprint(home.blueprint)
app.register_blueprint(login.blueprint)
app.register_blueprint(static.blueprint)
app.register_blueprint(logout.blueprint)
app.register_blueprint(password.blueprint)
app.register_blueprint(student.blueprint)













