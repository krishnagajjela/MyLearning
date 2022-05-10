import os
from requests_oauthlib import OAuth2Session

from flask import Flask, session, redirect, request

app = Flask(__name__)
app.secret_key = "fakdjfajdfijadfa"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# This information is obtained upon registration of a new GitHub
client_id = "k4IQRJNFAcMoXwRuSjpZ6S17Cx8W"
client_secret = "7c80eecc-2b56-4aaf-8c0b-b2644cfada81"
authorization_base_url = 'https://test-www.tax.service.gov.uk/oauth/authorize'
token_url = 'https://test-api.service.hmrc.gov.uk/oauth/token'
scope = "read:vat write:vat"
redirect_uri = 'http://localhost:5000/redirect-auth'

@app.route("/logintest")
def login():
    github = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = github.authorization_url(authorization_base_url)
    session['oauth_state']=state
    return redirect(authorization_url)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    return "Hello World <a href='/logintest'><button>Login</button></a>"


@app.route("/redirect-auth")
def protected_area():
    code = request.args.get("code")
    print(code)
    return f"Hello ! <br/> <a href='/logout'><button>Logout</button></a>"


if __name__ == "__main__":
    app.run(debug=True)
