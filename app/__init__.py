from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
from app.models import User
mail = Mail()
bootstap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    mail.init_app(app)


    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app