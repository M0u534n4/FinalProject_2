from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user,LoginManager
from form import SignUpForm, LoginForm
from models import User
from ext import app

login_manager = LoginManager()

user = [
    
]

views = Blueprint('views', __name__)

@app.route('/')
def  welcome():
    return render_template('index.html')



# @app.route('/user')
# def  user():
#     return render_template('pages/user_profile.html')




# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.query.filter(User.email == form.email.data).first()
#         if user and user.password == form.password.data:
#             login_user(user)

#     return render_template("pages/login.html", form=form)


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))


# @app.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     form = SignUpForm()   
#     if form.validate_on_submit():
#         user = User(email=form.email.data, password=form.password.data)
#         user.create()

#     return render_template("pages/sign_up.html", user=current_user, form=form)
