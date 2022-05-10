from flask import Flask, request, render_template
from screeninfo import get_monitors

DTestApp = Flask(__name__)

@DTestApp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        browserDetails_val = request.form.get('browserDetails')
        print("browserDetails Value is: ", browserDetails_val)
        x = browserDetails_val.split(":")
        print("Y values ")
        print(x)

    return render_template('index.html')

@DTestApp.route("/test1", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        browserDetails_val = request.form.get('browserDetails')
        print("browserDetails Value is: ", browserDetails_val)
        x = browserDetails_val.split(":")
        print("Z values ")
        print(x)

    return render_template('login.html')

def getKey():
    if request.method == 'POST':
        browserDetails_val = request.form.get('browserDetails')
        print("browserDetails Value is: ", browserDetails_val)
        A = browserDetails_val.split(":")
        print("A values ")
        print(A)
    return A

@DTestApp.route("/logout", methods=['GET', 'POST'])
def logout():
    val = getKey()
    return "logout "+val


if __name__ == '__main__':
    DTestApp.run(debug=True)
