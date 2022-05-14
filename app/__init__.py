from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app(app):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello world"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app