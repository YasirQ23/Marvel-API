
from werkzeug.security import generate_password_hash
from uuid import uuid4
from datetime import datetime
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


login = LoginManager()


@login.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key=True)
    username_id = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    wins = db.Column(db.Integer())
    losses = db.Column(db.Integer())
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))

    def __init__(self, username, email, password, first_name, last_name):
        self.username_id = username.lower()
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)
        self.wins = 0
        self.losses = 0


class CustomPokemon(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    type = db.Column(db.String(255), nullable=False)
    ability = db.Column(db.String(50))
    weight = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, dict):
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.type = dict['type']
        self.ability = dict['ability']
        self.weight = dict['weight']

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'ability': self.ability,
            'weight': self.weight,
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
