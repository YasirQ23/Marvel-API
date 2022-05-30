import requests as r
from flask_login import current_user
from app.models import Colections, User, MarvelCharacters

def col_creation():
    characters = []
    y = Colections.query.filter_by(user_id=current_user.id).all()
    for i in range(len(y)):
        x = y[i].marvelcharacters_id
        characters.append(MarvelCharacters.query.filter_by(id=x).first())
    return characters

