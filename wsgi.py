from flask import Flask, redirect, render_template, request, url_for
from utilities import password_match
from cruds import create_user


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    return "POST"


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        form_data = request.form
        if password_match(form_data.get('password1'), form_data.get('password2')):
            user = create_user(form_data.get('firstname'), form_data.get('lastname'), form_data.get(
                'phone'), form_data.get('email'), form_data.get('password1'))
            print(user)
            return redirect(url_for('login'))
        return 'password do not match', 401

        # print(form_data)
    return render_template('registration.html')
