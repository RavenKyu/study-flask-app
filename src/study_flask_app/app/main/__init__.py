import flask_login
from flask import Blueprint, render_template
from flask import request
from flask_login import login_required

main = Blueprint('main', __name__,
                 template_folder='templates',
                 static_folder='static')


@main.route('/')
@login_required
def index():
    if request.method == 'GET':
        return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    user = flask_login.current_user
    return render_template('profile.html', user=user)
