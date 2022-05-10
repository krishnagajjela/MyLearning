from flask import Flask, render_template, session, request, redirect
import sqlite3
from flask import g
import model.dbHandler as dbHandler


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

@app.route('/')
def login():
    return render_template("login.html")

@app.route("/mainPage", methods=['POST','GET'])
def check_login():
    userId = str(request.form.get('username'))
    password = str(request.form.get('password'))
    users = dbHandler.retrieveUsers()

    print("User entered UserName is: " + userId + "  User entered Password is: " + password)
    if request.method == 'POST':
        session['username'] = request.form['username']
        if userId == 'krishna' and password == 'user123':
            app.logger.info(userId+" user is logged in sucessfully.")
            return render_template('mainPage.html')
        else:
            return render_template('Invalid.html', info='Please Enter Correct UserName and Password')


@app.route('/logout')
def logout():
   session.clear()
   app.logger.info("User Logged Out Successfully")
   return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)