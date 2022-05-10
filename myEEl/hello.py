from __future__ import print_function	# For Py2/3 compatibility
import eel, js2py, execjs.runtime_names
from jinja2 import Markup
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
hello = Flask(__name__)
hello.secret_key = "randon key generation"


# Set templates files folder
# eel.init('templates')
#
#
# # eel.start('hello.html')    # Start
#
# @hello.route("/test")
# def testing():
#     @eel.expose  # Expose this function to Javascript
#     def say_hello_py(x, y, z):
#         print(x, y, z)
#     eel.start('hello.html')
#
#     return "hello.html"

@hello.route('/')
def login():
    return render_template("hello.html")

@hello.route('/process_qtc', methods=['POST', 'GET'])
def get_post_json():
    data = request.form.get("getD")
    print(data)
    return "Hello "+str(data)




if __name__ == "__main__":
    hello.run(debug=True)
