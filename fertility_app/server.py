"""Server for fertility app."""

from flask import Flask, render_template, request, flash, session, redirect
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


#  Creating this first route and view functions
@app.route("/")
def show_index():
    """Return homepage."""
    return render_template('homepage.html')


@app.route("/features")
def list_features():
    """Return page showing all the features app has to offer"""

    # feature_list = features.get_all()
    # if 'logged_in_user_id' not in  session:
    #     flash("Please login") 
    #     return redirect('/login')
    return render_template("all_features.html")#,
                        #    feature_list=feature_list)


@app.route("/temperatures", methods=["GET"])
def process_temperature():
    """Add user's temperature to DB """

    temperature = request.args.get('temperature')
    user_id = session['logged_in_user_id']
    # created_at = datetime.today())

    """MOve to crud"""
    new_temperature = Temperature(
                        user_id = user_id,
                        temperature_entry = int(temperature),
                        date_time = datetime.today())

    db.session.add(new_temperature)
    db.session.commit()

    return redirect('/features')

# @app.route("/features/<feature_id>")
# def show_feature(feature_id):
#     """Return page showing the details of a given feature.

#     Show info about a feature. Also, provide a button to enter the feature.
#     """

#     feature = feature.get_by_id(feature_id)
#     print(feature)
#     return render_template("feature_action.html",

    

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
    # print(first_name)


    user = User.query.filter_by(email = email).first()
    # print('smth here', confirm_password)
    if user:
        flash('An account with this email already exists')
        return redirect('/login')
    
    if password != confirm_password:
        flash('Password does not match, please try again')
        # return render_template('register.html')
        return redirect('/register')

    else:
        """Move to crud"""
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

        # first_time_user = User.query.filter_by(email = email).first()
        session['logged_in_user_id'] = new_user.user_id
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
            session['logged_in_user_id'] = user.user_id
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


# @app.route("/chart")
# def chart_build_test():
#     return render_template('chartjs.html')   

if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )