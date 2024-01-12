from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from form import SignUpForm, LoginForm
from models import User
from app import app


user = [
    
]

views = Blueprint('views', __name__)

@app.route('/')
def  welcome():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("pages/home.html", user=current_user)


@app.route('/user')
def  user():
    return render_template('pages/user_profile.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            redirect_url = request.args.get('next') or url_for('main.login')
            return redirect(redirect_url)

    return render_template("pages/login.html", user=current_user, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()   
    if form.validate_on_submit():
        user = User (email=form.email.data, password=form.password.data)
        user.create()
        return redirect(url_for('login'))

    return render_template("pages/sign_up.html", user=current_user, form=form)
