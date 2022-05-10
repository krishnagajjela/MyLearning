from flask import Flask, request, render_template

app1 = Flask(__name__)

@app1.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        browserDetails_val = request.form.get('browserDetails')
        print("browserDetails Value is: ", browserDetails_val)
        x = browserDetails_val.split(":")
        print(type(x))
        print(x)
    return render_template('testWebRTC.html')

if __name__ == '__main__':
    app1.run()
