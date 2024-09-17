from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_blueprint
from config.config import Config, db

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/register_form', methods=['GET'])
def register_form():
    return render_template('register.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
