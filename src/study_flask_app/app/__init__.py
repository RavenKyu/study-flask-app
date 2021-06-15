from flask import Flask


def create_app():
    app = Flask(__name__, )

    app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'

    # blueprint for auth routes in our app
    from study_flask_app.app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # # blueprint for non-auth parts of app
    from study_flask_app.app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
