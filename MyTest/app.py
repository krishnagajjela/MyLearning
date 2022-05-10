from datetime import datetime

import requests
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "randon key generation"

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('login.html', name=username)

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/getAge", methods=['GET', 'POST'])
def getAge():
    if request.method == 'POST':
        if request.form['getAge'] == 'getAge':
            age = request.form['age']
            session['age'] = age
            return render_template('about.html', age=age)

@app.route("/getName", methods=["GET", "POST"])
def getName():
    if 'age' in session:
        name = request.form.get("user")
        return render_template("about.html", name=name, age=session['age'])

@app.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == 'POST':
        redirect("movies.html")

@app.route("/movie_edit", methods=["GET", "POST"])
def movie_edit():
    if request.method == 'POST':
        redirect("movie_edit.html")


@app.route("/test")
def getHW():
    val = request.form.get("hw")
    print(val)
    redirect ("getScreen.html")

if __name__ == "__main__":
    app.run(debug=True)