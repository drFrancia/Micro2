import os 
from  flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret!'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_AUTH') or f'postgresql://sebastian:7501095@localhost:5432/auth' ## Preguntar si se puede haccer '/databases/product_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False