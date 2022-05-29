
from werkzeug.security import generate_password_hash
from uuid import uuid4
from datetime import datetime
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

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
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))
    marvelcharacters = relationship("MarvelCharacters", secondary="colections")

    def __init__(self, username, email, password, first_name, last_name):
        self.username_id = username.lower()
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)




class MarvelCharacters(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    comics_appeared_in = db.Column(db.Integer)
    super_power = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    image = db.Column(db.String(255))
    users = relationship("User", secondary="colections")

    def __init__(self, dict):
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.type = dict['description']
        self.ability = dict['comics appeared in']
        self.weight = dict['super power']
        self.image = dict['image']

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'comics appeared in': self.comics_appeared_in,
            'super power': self.super_power,
        }


    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)

class Colections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    marvelcharacters_id = db.Column(db.String, db.ForeignKey('marvel_characters.id'))
    user = relationship(User, backref=backref("colections", cascade="all, delete-orphan"))
    marvelcharacters = relationship(MarvelCharacters, backref=backref("colections", cascade="all, delete-orphan"))