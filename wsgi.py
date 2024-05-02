from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/login',methods= ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    return "POST"

@app.route('/registration',methods=['POST','GET'])
def registration():
    return render_template('registration.html')