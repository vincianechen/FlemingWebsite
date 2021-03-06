from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import schedule
engine = create_engine('sqlite:///flemingMembers.db', echo=True)
 
app = Flask(__name__)
error = None
currentID = None
 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    global error
    global currentID

    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
 
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
        result = query.first()
        if result:

            conn = engine.connect()
            res = conn.execute("select * from users where username = \"" + POST_USERNAME + "\"")
            for row in res:
                currentID = row['id']

            conn.close()
            session['logged_in'] = True
            session['user'] = POST_USERNAME
            error = None
            return home()
        else:
            session['logged_in'] = False
            print ("FOUND ERROR")
            error = "Invalid username or password. Try again."
    
    return render_template('login.html', error=error)
 
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/bylaws')
def bylaws():
    return render_template('bylaws.html')

@app.route('/directory')
def directory():

    conn = engine.connect()
    res = conn.execute("select * from info")
    data = []
    for row in res:
        data.append([row['firstName'], row['lastName'], row['year'], row['major'], row['location'], row['email'], row['id']])
    conn.close()
    return render_template('directory.html', data=data)

@app.route('/profile/<ID>')
@app.route('/profile')
def profile(ID=None):
    global currentID

    conn = engine.connect()

    error == True
    if ID == None:
        ID = currentID

    query = "select * from info where id=" + str(ID)
    res = conn.execute(query)
    data = []
    for row in res:
        data = [row['firstName'], row['lastName'], row['year'], row['major'], row['location'], row['email'], row['id']]
    conn.close()

    return render_template('profile.html', data=data, edit=True)

@app.route('/profile/<ID>/update', methods=['GET', 'POST'])
def profileUpdate(ID=None):

    if request.method == "POST":
        POST_FN = str(request.form['firstname'])
        POST_LN = str(request.form['lastname'])
        POST_YR = request.form['year']
        POST_MA = str(request.form['major'])
        POST_LOC = str(request.form['location'])
        POST_EM = str(request.form['email'])

        conn = engine.connect()
        query = "update info set firstName=\""+POST_FN+"\", lastName=\"" + POST_LN + "\" WHERE id=" +str(ID)
        res = conn.execute(query)
        conn.close()
    return profile(ID)


@app.route('/rotation')
def rotation():
    if session['logged_in'] == False:
        return render_template('home.html')

    return render_template('rotationHome.html')

@app.route('/attendance/<day>')
def attendance(day=None):
    if session['logged_in'] == False:
        return render_template('home.html')

    title = ""
    members = []

    (title, members) = schedule.returnDayInfo(day)

    return render_template('attendance.html', title=title, members=members)
 
@app.route('/quicksort')
def quicksort():
    if session['logged_in'] == False:
        return render_template('home.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)