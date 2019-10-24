import os
from flask import Flask, render_template, request, session
import pymysql
from flask_socketio import SocketIO, emit


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath('_file_'))
app.secret_key = "monnie0708068740daizy"
socketio = SocketIO(app)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # A default browser uses GET method by default
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "" or password == "":
            return render_template('login.html', msg1="* Empty credentials!!")

        con = pymysql.connect("localhost", "root", "", "transport")
        cursor = con.cursor()

        sql = "SELECT * FROM  `admin` WHERE username = %s AND password =%s"

        data = (username, password)

        cursor.execute(sql, data)
        # fetch data found
        if cursor.rowcount == 0:
            return render_template('login.html', msg1="*Login failed!")
        elif cursor.rowcount == 1:
            results = cursor.fetchall()
            session['x'] = username
            # store username in a session

            return render_template('adminhomepage.html', msg9="WELCOME TO TRANSPORT MANAGEMENT SYSTEM:", results=results)
        else:
            return render_template('login.html', msg1="*Error: Kindly Contact the Admin")

    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
        # A default browser uses GET method by default
        if request.method == 'POST':

            username = request.form['username']
            password = request.form['password']
            level = request.form['level']

            if username == "":
                return render_template('register.html', msg7="* please enter your username")
            if password == "":
                return render_template('register.html', msg8="* please enter your password")
            if level == "":
                return render_template('register.html', msg9="* please enter your Role")

            # connect to host and db

            con = pymysql.connect("localhost", "root", "", "transport")
            # cursor to excecute

            cursor = con.cursor()

            sql = "INSERT INTO `admin`(`username`,`password`, `level`) VALUES (%s,%s,%s)"

            # put values in a turple
            data = (username, password, level)

            # append your data to sql
            cursor.execute(sql, data)
            con.commit()  # commit changes
            return render_template('login.html', msg="SAVED SUCCESSFULLY")


        else:
            return render_template('register.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'x' in session:
    # A default browser uses GET method by default
        if request.method == 'POST':

            mobile = request.form['mobile']

            if mobile == "":
                return render_template('search.html', msg5="* please enter a phone number")

            con = pymysql.connect("localhost", "root", "", "transport")
            cursor = con.cursor()

            sql = "SELECT * FROM  `users` WHERE mobile = %s "

            data = (mobile)

            cursor.execute(sql, data)
            # fetch data found
            if cursor.rowcount < 1:
                return render_template('search.html', error="No Records Found")

            results = cursor.fetchall()

            return render_template('search.html', results=results)


        else:
            return render_template('search.html')
    else:
        return 'You are not logged in <a href = "/"> LOGIN HERE'


@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':

        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile = request.form['mobile']
        booking = request.form['booking']
        date = request.form['date']
        time = request.form['time']
        number = request.form['number']

        if fname == "":
            return render_template('booking.html', msg1="* please enter your first name")
        if lname == "":
            return render_template('booking.html', msg2="* please enter your last name")
        if email == "":
            return render_template('booking.html', msg3="* please enter your email")
        if mobile == "":
            return render_template('booking.html', msg4="* please enter your phone number")
        if booking == "":
            return render_template('booking.html', msg5="* please enter booking number")
        if date == "":
            return render_template('booking.html', msg6="* please enter the date to travel")
        if time == "":
            return render_template('booking.html', msg7="* please enter the time to travel")
        if number == "":
            return render_template('booking.html', msg8="* please enter the Mpesa confirmation number")

        con = pymysql.connect("localhost", "root", "", "transport")
        cursor = con.cursor()

        sql = "INSERT INTO `users`(`fname`, `lname`, `email`, `mobile`, `booking`, `date`, `time`, `number`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (fname, lname, email, mobile, booking, date, time, number)
        cursor.execute(sql, data)
        con.commit()
        return render_template('booking.html', msg="SAVED SUCCESSFULLY")

    else:
        return render_template('booking.html')

@app.route('/twowaybooking', methods=['GET', 'POST'])
def two_way_booking():
    if request.method == 'POST':

        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile = request.form['mobile']
        booking = request.form['booking']
        date = request.form['date']
        time = request.form['time']
        number = request.form['number']

        if fname == "":
            return render_template('two way booking.html', msg1="* please enter your first name")
        if lname == "":
            return render_template('two way booking.html', msg2="* please enter your last name")
        if email == "":
            return render_template('two way booking.html', msg3="* please enter your email")
        if mobile == "":
            return render_template('two way booking.html', msg4="* please enter your phone number")
        if booking == "":
            return render_template('two way booking.html', msg5="* please enter booking number")
        if date == "":
            return render_template('two way booking.html', msg6="* please enter the date to travel")
        if time == "":
            return render_template('two way booking.html', msg7="* please enter the time to travel")
        if number == "":
            return render_template('two way booking.html', msg8="* please enter the Mpesa confirmation number")

        con = pymysql.connect("localhost", "root", "", "transport")
        cursor = con.cursor()

        sql = "INSERT INTO `users`(`fname`, `lname`, `email`, `mobile`, `booking`, `date`, `time`, `number`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (fname, lname, email, mobile, booking, date, time, number)
        cursor.execute(sql, data)
        con.commit()
        return render_template('two way booking.html', msg="SAVED SUCCESSFULLY")

    else:
        return render_template('two way booking.html')


@app.route('/admin')
def admin():
    return render_template('Admin.html')


@app.route('/adminhomepage')
def adminhomepage():
    return render_template('adminhomepage.html')

@app.route( '/complaints' )
def complaints():
   return render_template('complaints.html')

def messageRecived():
  print( 'message was received!!!' )

@socketio.on('my event')
def handle_my_custom_event(json):
  print('received my event: ' + str(json))
socketio.emit('my response', callback=messageRecived)

@app.route('/logout')
def logout():
     session.pop('x',None) # clear session 'x'
     return render_template('login.html')

if __name__ == '__main__':
    app.run(debug='true')
    socketio.run(app)

