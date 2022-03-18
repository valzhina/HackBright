"""Server for fertility app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from datetime import datetime, date, time

from model import connect_to_db, db, User, Temperature, Supplement, Meal
# import crud

from jinja2 import StrictUndefined


app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined

# app.jinja_env.auto_reload = True

MOST_LOVED_ACTIVITY = {
    "kate": {
        "img": "https://unsplash.com/photos/uM18y03NkNg",
        "name": "Kate_Hliznitsova",
        "num_loves": 3,
    },
}

#  Creating this first route and view functions
@app.route("/")
def show_index():
    """Return homepage."""
    # if 'name' in session:
    #     return redirect("/features")
    return render_template('homepage.html')


@app.route("/features")
def list_features():
    """Return page showing all the features app has to offer"""

    # feature_list = features.get_all()
    return render_template("all_features.html")#,
                        #    feature_list=feature_list)


@app.route("/features/<feature_id>")
def show_feature(feature_id):
    """Return page showing the details of a given feature.

    Show info about a feature. Also, provide a button to enter the feature.
    """

    #DM: replaced ... to melon_id
    feature = melons.get_by_id(melon_id)
    print(melon)
    return render_template("melon_details.html",
                           display_melon=melon)

# @app.route("/get-name")
# def get_name():
#     session['name'] = request.args["name"]
    
#     return redirect('/all_features')


# @app.route("/more_features")
# def top_activities():
#     """Return page showing top activities"""
#     if 'name' in session:
#         return render_template("first-page.html", activity = MOST_LOVED_ACTIVITY)
#     return redirect("/")
    

# User Routs...
@app.route("/register", methods=["GET"])
def show_register():
    """Show register form."""
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def process_register():
    """Register user information to DB """

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('re_password')


    user = User.query.filter_by(email = email).first()

    if user != None:
        flash('An account with this email already exists')
        return redirect('/login')
    
    if password != confirm_password:
        flash('Password does not match, please try again')

    else:
        new_user = User(first_name = first_name,
                        last_name = last_name,
                        email = email,
                        password = password,
                        # profile_proto_url
                        created_at = datetime.today())
    
        # set password for new user
        # set password securely
        
        db.session.add(new_user)
        db.session.commit()

        first_time_user = User.query.filter_by(email = email).first()
        session['logged_in_user_id'] =  first_time_user.user_id
        flash('Login successful')

    return redirect('/features')
        

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
            session['logged_in_customer_name'] = user.first_name
            flash('Login successful')
            return redirect('/features')
        else:
            flash('Incorrect password')
            
    else:
        flash('Incorrect login')

    return redirect('/login')


@app.route("/logout")
def process_logout():
    del session['logged_in_customer_name']
    flash("Logged out")
    return redirect('homepage.html')   



if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )