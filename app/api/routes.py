from app.models import MarvelCharacters, db
from .services import token_required
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/marvelcharacters', methods=['GET'])
def getMarvelCharacters():
    marvelcharacter = MarvelCharacters.query.all()
    marvelcharacter = {a.id: a.to_dict() for a in marvelcharacter}
    return jsonify(marvelcharacter), 200


@api.route('/marvelcharacters/<string:name>', methods=['GET'])
def MarvelCharactersName(name):
    print(name)
    marvelcharacters = MarvelCharacters.query.filter_by(name=name.title()).first()
    if marvelcharacters:
        return jsonify(marvelcharacters.to_dict()), 200
    return jsonify({'error': f'no such marvel character with the name: {name.title()}'}), 404


@api.route('/create', methods=['POST'])
# @token_required
def createMarvelCharacters():
    try:
        newdict = request.get_json()
        print(newdict)
        a = MarvelCharacters(newdict)
        print(a)
    except:
        return jsonify({'error': 'improper request or body data'}), 400
    try:
        db.session.add(a)
        db.session.commit()
    except:
        return jsonify({'error': 'marvel character already exists in the database'}), 400
    return jsonify({'created': a.to_dict()}), 200

