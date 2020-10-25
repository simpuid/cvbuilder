from flask import render_template, Blueprint

blueprint = Blueprint('static', __name__)


@blueprint.route('/sharam')
def handle_sharam():
    return render_template('sharam.html'), 403


@blueprint.errorhandler(404)
def handle_404(e):
    return render_template("404_error.html"), 404