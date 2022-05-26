from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user

battle = Blueprint('battle', __name__, template_folder='battle_templates',
                   url_prefix='/battle', static_folder='battle_static')


@battle.route('/menu', methods=['GET', 'POST'])
@login_required
def menu():
    return render_template('menu.html')


@battle.route('/win', methods=['GET', 'POST'])
@login_required
def win():
    return render_template('win.html')


@battle.route('/lose', methods=['GET', 'POST'])
@login_required
def lose():
    return render_template('lose.html')
