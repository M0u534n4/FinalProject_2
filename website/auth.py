from flask import Blueprint, render_template, render_template_string, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('pages/login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('passwird2')

        if len(firstName) < 2:
            flash('First name must be bigger than 2 cherecters.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be bigger than 2 cherecters.', category='error')
        elif len(email) < 4:
            flash('Email must be bigger than 4 cherecters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Passwords must be bigger than 7 cherecters.', category='error')
        else:
            flash('Account created!', category='success')
    return render_template('pages/sign-up.html', )