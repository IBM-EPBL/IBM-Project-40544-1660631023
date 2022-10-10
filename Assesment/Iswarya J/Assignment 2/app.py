from flask import Flask,url_for,render_template

app=Flask(__name__)
@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/aboutpage")
def Aboutpage():
    return render_template('about.html')
@app.route("/signin")
def signin():
    return render_template('signin.html')
@approute("/login")
def login():
    return render_template('login.html')
