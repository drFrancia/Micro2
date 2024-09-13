from flask import Flask
from flask_jwt_extended import JWTManager
from src.auth_routes.auth_routes import auth_blueprint
from config.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app. config.from_object(Config)

jwt = JWTManager(app)
db = SQLAlchemy(app)

app.register_blueprint(auth_blueprint, url_prefix = '/auth')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0' port=5001) #falta el metodo run kkkkk