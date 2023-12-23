from flask import Blueprint, render_template

views = ('views', __name__)

@views.route('/')
def  welcome():
    return render_template('index.html')

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('pages/home.html')

@views.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('pages/user_profile.html')