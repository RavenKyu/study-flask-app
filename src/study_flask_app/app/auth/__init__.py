from flask import Blueprint, render_template, flash, session
from flask import Response, redirect, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from study_flask_app import users

auth = Blueprint('auth', __name__,
                 template_folder='templates',
                 static_folder='static')


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = next(x for x in users if x.email == email)
            if not check_password_hash(user.password, password):
                raise StopIteration
        except StopIteration:
            flash('Username or Password Incorrect', "message")
            return render_template('login.html')

        login_user(user)
        session['logged_in'] = True
        session['email'] = user.email
        session['user_name'] = user.name

        next_path = request.args.get("next")
        if not next_path:
            next_path = '/'
        return redirect(next_path)

    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


# somewhere to logout
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    session['logged_in'] = False
    session['email'] = ''
    session['user_name'] = ''
    return redirect(url_for('main.index'))
