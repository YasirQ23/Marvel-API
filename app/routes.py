from app import app

from flask import render_template

import requests as r
from .services import lib_creation

@app.route('/')
def creation():
    poke_list=lib_creation()
    return render_template('index.html',poke_list=poke_list)

@app.route('/gen-1')
def gen_1():
    poke_list=lib_creation()
    return render_template('gen-1.html',poke_list=poke_list)

@app.route('/gen-2')
def gen_2():
    poke_list=lib_creation()
    return render_template('gen-2.html',poke_list=poke_list)

@app.route('/gen-3')
def gen_3():
    poke_list=lib_creation()
    return render_template('gen-3.html',poke_list=poke_list)
