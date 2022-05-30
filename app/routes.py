from typing import Collection
from app import app
from app.models import Colections, User, MarvelCharacters, db
from flask import render_template, flash, redirect, url_for
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

@app.route('/add/<string:id>')
def addMarvelCharacter(id):
    if len(Colections.query.filter_by(user_id=current_user.id).all()) == 3:
        flash(f'Character Collection Max Is 3 Please Remove A Character To Add', 'danger')
        return redirect(url_for('mycollection'))
    marvelcharacter = Colections(current_user.id, id)
    db.session.add(marvelcharacter)
    db.session.commit()
    flash(f'Character Added', 'primary')
    return redirect(url_for('mycollection'))



@app.route('/delete/<string:id>')
def removeMarvelCharacter(id):
    character = Colections.query.filter_by(user_id=current_user.id).all()
    for i in range(len(character)):
        if id == character[i].marvelcharacters_id:
            db.session.delete(character[i])
            db.session.commit()
    flash(f'Character Removed', 'danger')
    return redirect(url_for('mycollection'))
