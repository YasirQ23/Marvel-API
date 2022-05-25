from flask import Blueprint, jsonify 

api = Blueprint('api',__name__,url_prefix='/api')

@api.route('/test', methods=['GET'])
def test():
    return jsonify('testing some data'), 200