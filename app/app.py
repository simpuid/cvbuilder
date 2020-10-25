from flask import *
from flask_bootstrap import Bootstrap

from db import *
from flask_login import LoginManager
from config import AppConfig
from tables import *
from routes import home, login, logout, password, student

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
app.register_blueprint(logout.blueprint)
app.register_blueprint(password.blueprint)
app.register_blueprint(student.blueprint)


@app.errorhandler(404)
def handle_404(e):
    return render_template("404_error.html"), 404


@app.route('/sharam')
def handle_sharam():
    return render_template('sharam.html'), 403
