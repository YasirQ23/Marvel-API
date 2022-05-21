from app import app

from flask import render_template

import requests as r
from .services import lib_creation

@app.route('/')
def creation():
    poke_list=lib_creation()
    return render_template('index.html',poke_list=poke_list)

@app.route('/bulbasaur')
def bulbasaur():
    poke_list=lib_creation()
    return render_template('bulbasaur.html',poke_list=poke_list)

@app.route('/charmander')
def charmander():
    poke_list=lib_creation()
    return render_template('charmander.html',poke_list=poke_list)

@app.route('/squirtle')
def squirtle():
    poke_list=lib_creation()
    return render_template('squirtle.html',poke_list=poke_list)
