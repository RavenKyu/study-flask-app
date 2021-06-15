from study_flask_app.app import create_app
from flask_login import LoginManager
from study_flask_app import users


def main():
    app = create_app()
    # flask-login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return next(x for x in users if x.id == int(user_id))
        except StopIteration:
            return None

    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    main()
