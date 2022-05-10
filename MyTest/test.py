from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
test = Flask(__name__)
test.secret_key = "random key generation here"

@test.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))

@test.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'

if __name__ == "__main__":
    test.run(debug=True)