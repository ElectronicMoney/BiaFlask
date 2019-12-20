from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.home import home
    from app.users import users

    app.register_blueprint(home)
    app.register_blueprint(users)

    return app