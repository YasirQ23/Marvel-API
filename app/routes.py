from app import app
from app.models import Colections, User, MarvelCharacters
from flask import render_template, flash
from flask_login import current_user

import requests as r
from flask_login import login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mycollection')
def mycollection():
    characters = MarvelCharacters.query.all()
    return render_template('mycollection.html', characters=characters)

@app.route('/marvelcharecters')
def marvelcharecters():
    characters = MarvelCharacters.query.all()
    return render_template('marvelcharecters.html', characters=characters)

