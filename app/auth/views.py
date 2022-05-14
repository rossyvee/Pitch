
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app.auth import auth

@auth.route('/login')
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        print(username)
        user = User.query.filter_by(username=username).first()
        if user is None:
            error = 'user does not exist'
            return render_template('login.html', error=error)
        is_correct_password = user.check_password(password)
        print(is_correct_password)
        if not is_correct_password:
            error = ' password error'
            return render_template('login.html', error=error)
        login_user(user)
        return redirect('/')
    return render_template('login.html')


@auth.route('/sign-up')
def sign_up():
 if request.method == 'POST':
        form = request.form
        username = form.get("username")
        email = form.get("email")
        password = form.get("password")
        confirm_password = form.get("confirm_password")
        if username is None or password is None or email is None or confirm_password is None:
            error = 'username, email, password are required'
            return render_template('signup.html', error=error)
        if ' ' in username:
            error = 'Username should not contain spaces'
            return render_template('signup.html', error=error)
        if password != confirm_password:
            error = "Passwords do not match"
            return render_template('signup.html', error=error)
        else:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                error = 'A user with that name already exists'
                return render_template('signup.html', error=error)
            user = User.query.filter_by(email=email).first()
            if user is not None:
                error = 'A user with that email already exists'
                return render_template('signup.html', error=error)
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # email_message("Welcome to 1m Pitch", "email/howdy", user.email, user=user)
            return redirect(url_for('auth.login'))

@auth.route('/sign-out')
def login_out():
   return render_template('log_out.html')