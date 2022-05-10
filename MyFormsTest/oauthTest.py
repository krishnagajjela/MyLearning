from requests_oauthlib import OAuth2Session

import os
from flask import Flask, request, redirect, session


# This information is obtained upon registration of a new GitHub
client_id = "k4IQRJNFAcMoXwRuSjpZ6S17Cx8W"
client_secret = "7c80eecc-2b56-4aaf-8c0b-b2644cfada81"
authorization_base_url = 'https://test-www.tax.service.gov.uk/oauth/authorize'
token_url = 'https://test-api.service.hmrc.gov.uk/oauth/token'
scope = "read:vat write:vat"
redirect_uri = 'http://localhost:5000/redirect'

app = Flask(__name__)
app.secret_key = "dkfadhfjadfkafkja"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

@app.route("/login")
def login():
    github = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state

    return redirect(authorization_url)

@app.route("/redirect")
def callback():
    github = OAuth2Session(client_id, state=session['oauth_state'], redirect_uri=redirect_uri)

    token = github.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)

    session["oauth_token"] = token

    return redirect("/protected_area")

@app.route("/protected_area")
def protected_area():
    return f"Hello! <br/> <a href='/logout'><button>Logout</button></a>"

@app.route("/")
def index():
    return "Hello World <a href='/login'><button>Login</button></a>"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)