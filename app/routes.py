from app import app

from flask import render_template, flash

import requests as r
from .services import lib_creation_gen1
from flask_login import login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mycollection')
def mycollection():
    return render_template('mycollection.html')

@app.route('/marvelcharecters')
def marvelcharecters():
    return render_template('marvelcharecters.html')

