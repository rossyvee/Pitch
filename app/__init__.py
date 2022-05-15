from flask import Flask 
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
mail = Mail()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
   #creating configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extentions
    bootstap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #registering the blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app