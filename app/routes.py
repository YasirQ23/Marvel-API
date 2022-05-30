from app import app
from app.models import Colections, User, MarvelCharacters, db
from flask import render_template, flash
from flask_login import current_user

import requests as r
from flask_login import login_required
from .services import col_creation

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mycollection')
def mycollection():
    characters = col_creation()
    return render_template('mycollection.html', characters=characters)

@app.route('/marvelcharecters')
def marvelcharecters():
    characters = MarvelCharacters.query.all()
    return render_template('marvelcharecters.html', characters=characters)

# @app.route('/delete/<string:id>')
# def removeMarvelCharacter(id):
#     character = Colections.query.filter_by(user_id=current_user.id,	marvelcharacters_id=id)
#     if not character:
#         flash(f'Character Not Removed')
#         return render_template('mycollection.html')
#     db.session.delete(character)
#     db.session.commit()
#     flash(f'Character Removed', 'danger')
#     return render_template('mycollection.html')
