from app import app

from flask import render_template, flash

import requests as r
from .services import lib_creation_gen1, lib_creation_gen2, lib_creation_gen3
from flask_login import login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gen-1')
def gen_1():
    poke_list=lib_creation_gen1()
    return render_template('gen-1.html',poke_list=poke_list)

@app.route('/gen-2')
def gen_2():
    poke_list=lib_creation_gen2()
    return render_template('gen-2.html',poke_list=poke_list)

@app.route('/gen-3')
def gen_3():
    poke_list=lib_creation_gen3()
    return render_template('gen-3.html',poke_list=poke_list)
