from config.config import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_keu = True)
    username = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(200), nullable = False)
