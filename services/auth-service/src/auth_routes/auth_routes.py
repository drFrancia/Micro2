from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods = 'POST')
def register():
    data = request.get_json()
    return AuthService.register(data)


@auth_blueprint.route('/login', methods = 'POST')
def login():
    data = request.get_json()
    return AuthService.login(data)