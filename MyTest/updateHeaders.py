from datetime import datetime

import requests
from flask import Flask, render_template, request, redirect, url_for, session
hUpdate = Flask(__name__)
hUpdate.secret_key = "randon key generation"

fraud_prevention_headers_list = {"Accept": "application/vnd.hmrc.1.0+json",
                                 "Gov-Client-Connection-Method": "WEB_APP_VIA_SERVER",
                                 "Gov-Client-Browser-Do-Not-Track": "false"}

s = requests.session()
s.headers.update(fraud_prevention_headers_list)


@hUpdate.route("/")
def aboutPage():
    return render_template("about.html")

@hUpdate.route("/getAge", methods=['GET', 'POST'])
def getAge():
    if request.method == 'POST':
        if request.form['getAge'] == 'getAge':
            age = request.form['age']
            session['age'] = age
            test = {"Name": "Krishna"}
            s.headers.update(test)
            print(s.headers)

            return render_template('about.html', age=age)

@hUpdate.route("/getName", methods=["GET", "POST"])
def getName():
    if 'age' in session:
        name = request.form.get("user")
        return render_template("about.html", name=name, age=session['age'])

@hUpdate.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == 'POST':
        redirect("movies.html")

@hUpdate.route("/movie_edit", methods=["GET", "POST"])
def movie_edit():
    if request.method == 'POST':
        redirect("movie_edit.html")


@hUpdate.route("/test")
def getHW():
    val = request.form.get("hw")
    print(val)
    redirect ("getScreen.html")

if __name__ == "__main__":
    hUpdate.run(debug=True)