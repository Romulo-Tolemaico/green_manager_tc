from flask import Blueprint,jsonify,request

main = Blueprint('user_blueprint', __name__)

@main.route('/demo')
def demo():
    return "<h1> Hola mundo jajaja </h1>"

