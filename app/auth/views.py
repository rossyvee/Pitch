
from flask import flash, render_template, request, redirect, url_for
from app import auth
from flask_login import login_user, logout_user



@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    return render_template('auth/login.html', loginform = form)


@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
   form = RegForm()
   if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save_u()
        mail_message("Welcome to Pitch-World","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
        return render_template('auth/signup.html', r_form = form)


@auth.route('/sign-out', methods = ['GET','POST'])
def login_out():

   return render_template('log_out.html')