from . import auth

@auth.route('/login')
def login():
    return "Login"

@auth.route('/sign-up')
def sign_up():
    return "Sign-up"

@auth.route('/sign-out')
def login_out():
    return "Log-out"