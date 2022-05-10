from flask import g, Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    x1 = 100
    g.x1 = x1
    return "<h1>index</h1>"


@app.route("/login")
def login():
    print(x1)
    return "<h1>login success</h1>"

@app.route("/login1")
def login1():
    print(g.get('x1'))
    return "<h1>sucess</h1>"

if __name__ == "__main__":
    app.run(debug=True)