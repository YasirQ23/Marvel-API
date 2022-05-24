from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth', static_folder='auth_static')

from .authforms import RegistrationForm, LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
            if form.validate_on_submit():
                flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
                return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.data)
            print(form.email.data)
            flash('Welcome! Thank you for registering!', 'info')
            return redirect(url_for('auth.register'))
        else:
            flash('Sorry, passwords do not match. Please try again.', 'danger')
            return redirect(url_for('auth.register'))
    elif request.method == 'GET':
        return render_template('register.html', form=form)