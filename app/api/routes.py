from app.models import CustomPokemon, db
from .services import token_required
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test', methods=['GET'])
def test():
    pokemon = CustomPokemon.query.all()[0]
    return jsonify(pokemon.to_dict()), 200


@api.route('/custompokemons', methods=['GET'])
def getcustompokemons():
    custompokemon = CustomPokemon.query.all()
    print(custompokemon)
    custompokemon = {a.id: a.to_dict() for a in custompokemon}
    return jsonify(custompokemon), 200


@api.route('/custompokemons/<string:name>', methods=['GET'])
def getCustomPokemonName(name):
    print(name)
    custompokemons = CustomPokemon.query.filter_by(name=name.title()).first()
    if custompokemons:
        return jsonify(custompokemons.to_dict()), 200
    return jsonify({'error': f'no such pokemon with the name: {name.title()}'}), 404


@api.route('/create', methods=['POST'])
@token_required
def createCustomPokemon():
    try:
        newdict = request.get_json()
        print(newdict)
        a = CustomPokemon(newdict)
        print(a)
    except:
        return jsonify({'error': 'improper request or body data'}), 400
    try:
        db.session.add(a)
        db.session.commit()
    except:
        return jsonify({'error': 'pokemon already exists in the database'}), 400
    return jsonify({'created': a.to_dict()}), 200

