from flask import Flask, request, render_template
import datetime
import logging
import os

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    log_level = logging.INFO

    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)

    root = os.path.dirname(os.path.abspath(__file__))
    today = datetime.datetime.now()
    formatvalue = today.strftime("%d-%B-%Y_%H_%M_%S")
    logFileName = "Log_"+formatvalue+".log"
    logdir = os.path.join(root, 'logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    log_file = os.path.join(logdir, logFileName)
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

@app.route("/")
def testButton():
    app.logger.info('TestLink Clicked.')
    return render_template("TestLink.html")

@app.route("/finalTest", methods=["GET", "POST"])
def finalTest():
    if request.form.get("login"):
        user = request.form.get("input")
        app.logger.info("login button clicked.")
        return render_template("pageLogin.html", user=user )

    if request.form.get("signUp"):
        user = request.form.get("input")
        app.logger.info("SignUp button clicked.")
        return render_template("pageSignUp.html", user=user )

if __name__ == "__main__":
    app.run()