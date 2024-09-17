from flask import Blueprint, request, redirect, url_for, render_template
from services.auth_service import AuthService

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['GET'])
def show_register_form():
    return render_template('register.html') 

@auth_blueprint.route('/register', methods = ['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    data = {
        'username': username,
        'email': email,
        'password': password
    }
    response = AuthService.register(data)

    if response['success']:
        return redirect(url_for('auth.show_login_form'))  # haver un login.html
    else:
        return render_template('register.html', error=response['message'])



@auth_blueprint.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    return AuthService.login(data)