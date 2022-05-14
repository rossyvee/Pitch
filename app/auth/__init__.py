from flask import Blueprint
auth = Blueprint('auth',__name__)


@auth.route('/login')
def login():
    return "Login"

@auth.route('/sign-up')
def sign_up():
    return "Sign-up"

@auth.route('/sign-out')
def login_out():
    return "Log-out"