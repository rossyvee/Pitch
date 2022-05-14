from flask import Blueprint
auth = Blueprint('auth',__name__)


@auth.route('/login')
def home():
    return "Home"