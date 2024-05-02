from flask import Flask, redirect, render_template, request, url_for, session
from utilities import password_match
from cruds import create_user, is_valid_user
import os
from auth import session_required


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/')
@app.route('/home')
@session_required
def home():
    return session.get('user_id') + ' You are authenticated'

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    redirect(url_for('landing_page.html'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('user_id',None)
    if request.method == "POST":
        user_credentials = request.form
        user = is_valid_user(user_credentials.get('email'),
                         user_credentials.get('password'))
        if user:
            session['user_id'] = user.credential
            return redirect(url_for('home'))

    return render_template('login.html')


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
