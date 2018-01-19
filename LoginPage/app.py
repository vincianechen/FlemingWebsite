from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///flemingMembers.db', echo=True)
 
app = Flask(__name__)
error = None
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html', error=error)
    else:
        return render_template('home.html')
        # "Hello Boss!  <a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    global error

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        error = None
    else:
        print ("FOUND ERROR")
        error = "Invalid username or password. Try again."
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)