from flask import Flask, request, render_template
from screeninfo import get_monitors

DTestAnotherApp = Flask(__name__)

def testing():
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height
    if request.method == 'POST':
        browserDetails_val = request.form.get('browserDetails')
        print("browserDetails Value is: ", browserDetails_val)
        x = browserDetails_val.split(":")
        print(type(x))
        print(x, width, height)
        return x

@DTestAnotherApp.route("/test1", methods=['GET', 'POST'])
def login():
    print("login page values ")
    print(y)
    return "Login page"

@DTestAnotherApp.route('/', methods=['GET', 'POST'])
def index():
    global y
    y = testing()
    print("Y values ")
    print(y)
    return render_template('index.html')

if __name__ == '__main__':
    DTestAnotherApp.run(debug=True)
