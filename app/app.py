from flask import *
from flask_bootstrap import Bootstrap
from db import *
from flask_login import LoginManager
from config import AppConfig
from models import *
from routes import *

if initialize('cv_data', 'init.sql'):
    populate_users()
    populate_professors()

app = Flask(__name__)
app.config.from_object(AppConfig)
Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login.login'


@login_manager.user_loader
def load_user(uid):
    return User.load(int(uid))


@app.errorhandler(404)
def handle_404(e):
    app.logger.warning(e.description)
    return render_template("404_error.html"), 404


@app.route('/sharam')
def handle_sharam():
    return render_template('sharam.html'), 403


app.register_blueprint(home.blueprint)
app.register_blueprint(login.blueprint)
app.register_blueprint(logout.blueprint)
app.register_blueprint(password.blueprint)
app.register_blueprint(student.blueprint)
app.register_blueprint(tenth.blueprint)
app.register_blueprint(twelfth.blueprint)
app.register_blueprint(skill.blueprint)
app.register_blueprint(achievement.blueprint)
app.register_blueprint(language.blueprint)
app.register_blueprint(extra_curricular.blueprint)
app.register_blueprint(reference.blueprint)
app.register_blueprint(sgpa.blueprint)
app.register_blueprint(internship.blueprint)
app.register_blueprint(generate.blueprint)
app.register_blueprint(download.blueprint)
app.register_blueprint(dashboard.blueprint)
app.register_blueprint(project.blueprint)
