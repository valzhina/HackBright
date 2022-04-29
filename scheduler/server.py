"""Server for Scheduler app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from datetime import datetime, date, time, timedelta

from sqlalchemy import Date

from model import connect_to_db, db, User, Appointment
# import crud

from jinja2 import StrictUndefined

import os


app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined

# app.jinja_env.auto_reload = True


#########################################################################
#                     HOMEPAGE                             #
#########################################################################


#  Creating this first route and view functions
@app.route("/")
def show_index():
    """Return login."""

    if 'logged_in_user_id' not in session:
        flash("Please login") 
        return redirect('/login')

    return render_template('homepage.html')


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email = email).first()
  
    if user:
        if password == user.password:
            session['logged_in_user_id'] = user.user_id
            session['logged_in_user_name'] = user.first_name
            flash('Login successful')
            return redirect('/')
        else:
            flash('Incorrect password')
    else:
        flash('Incorrect login')

    return redirect('/login')

@app.route("/schedule", methods=["POST"])
def get_schedule():
    
    user_id = session['logged_in_user_id']

    req_date = request.json.get('req_date')
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')

    print("\n\n\n")
    print(req_date, start_time, end_time)
    print("\n\n\n")

    apps = Appointment.query.filter_by(user_id = user_id, date = req_date).all()
    
    occupied_spots = []
    for app in apps:
        occupied_spots.append(app.time)
    
    available_spots = [t for t in range(9,18) if t not in occupied_spots]


    return jsonify({'available':available_spots})







@app.route("/logout")
def process_logout():
    del session['logged_in_user_id']
    del session['logged_in_user_name']
    flash("Logged out")
    return redirect('/')   

 

if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )