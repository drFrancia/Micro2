from flask import jsonify
from models.user import User
from config.config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def register(data):
        if User.query.filter_by(email=data['email']).first():
            return jsonify({"message": "Usuario ya registrado"}), 400
        
        hashed_password = generate_password_hash(data['password'])
        new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Usuario registrado exitosamente"}), 201

    @staticmethod
    def login(data):
        user = User.query.filter_by(email=data['email']).first()
        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({"message": "Credenciales incorrectas"}), 401
        
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token), 200
