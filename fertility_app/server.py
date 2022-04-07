"""Server for fertility app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from datetime import datetime, date, time, timedelta

from sqlalchemy import Date, cast

from model import connect_to_db, db, User, Temperature, Supplement, Meal, Menstruation, Notes, Water
# import crud

from jinja2 import StrictUndefined

import cloudinary.uploader
import os

CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "dujmljv3d"

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
#                     HOMEPAGE AND FEATURES                             #
#########################################################################


#  Creating this first route and view functions
@app.route("/")
def show_index():
    """Return homepage."""
    return render_template('homepage.html')


@app.route("/features")
def list_features():
    """Return page showing all the features app has to offer"""

    # feature_list = features.get_all()
    if 'logged_in_user_id' not in  session:
        flash("Please login") 
        return redirect('/login')
    return render_template("all_features.html")#,
                        #    feature_list=feature_list)


#########################################################################
#                         TEMPERATURE                                   #
#########################################################################


@app.route("/temperatures", methods=["GET"])
def process_temperature():
    """Add user's temperature to DB """

    temperature = request.args.get('temperature')
    tdate = request.args.get('tdate')
    user_id = session['logged_in_user_id']
    # created_at = datetime.today())
    print(tdate)
    
    """Move to crud"""
    new_temperature = Temperature(
                        user_id = user_id,
                        temperature_entry = float(temperature),
                        temp_date = tdate)
    
    db.session.add(new_temperature)
    db.session.commit()

    return redirect('/features')


@app.route("/charts")
def process_temperature_chart():
    """Get temperature details from db and render it"""

    user_id = session['logged_in_user_id']

    temperature_details = Temperature.query.filter(Temperature.user_id == user_id).all()
    
    dates = []
    temps = []
    
    for entry in temperature_details:
        dates.append(entry.temp_date)
        temps.append(float(entry.temperature_entry))

    return render_template("chartjs.html", temperature_list = temps, temp_dates_list = dates)



#########################################################################
#                         SUPPLEMENTS                                   #
#########################################################################


@app.route("/supplements", methods=["GET"])
def process_supplement():
    """Add user's supplement to DB """

    supplement = request.args.get('supplement')
    supplement_time = request.args.get('supp_time')
    supplement_dose = request.args.get('supp_dose')
    supplement_dose_type = request.args.get('supp_dose_type')
    # date_started = request.args.get('date_started')

    user_id = session['logged_in_user_id']
    # print(supplement,supplement_dose, supplement_time)

    """Move to crud"""
    new_supplement = Supplement(
                        user_id = user_id,
                        supplement_entry = supplement,
                        supplement_dose = supplement_dose,
                        supplement_dose_type = supplement_dose_type,
                        supplement_time = supplement_time)
                        # date_started = date_started

    db.session.add(new_supplement)
    db.session.commit()

    return redirect('/features')


@app.route("/supp_charts")
def process_supplements_chart():
    """Get supplements details from db and render it"""

    user_id = session['logged_in_user_id']

    supplement_details = Supplement.query.filter(Supplement.user_id == user_id).all()
    
    # supp = []
    # supp_dose = []
    # supp_dose_type = []
    supp_time = []
    
    for entry in supplement_details:
        # supp.append(entry.supplement_entry)
        # supp_dose.append(entry.supplement_dose)
        # supp_dose_type.append(entry.supplement_dose_type)
        supp_time.append(entry.supplement_time)

    supp_time_unique = list(set(supp_time))

    # return render_template("chart_supp.html", supplement = supp, s_dose = supp_dose, s_type = supp_type, supplement_details = supplement_details)
    # return render_template("chart_supp.html", data = jsonify({'supplement': supp, 'dose': supp_dose, 'dose_type': supp_dose_type, 'dose_time': supp_time}))
    return render_template("chart_supp.html", data = supplement_details, supp_time_unique = supp_time_unique)



#########################################################################
#                        Meal Journal                                   #
#########################################################################


# @app.route("/meal_journal")
# def show_meal_journal():
#     """Return Meal Page"""
#     return render_template('meals.html')

@app.route("/meal_info_day", methods = ["POST"])
def get_meals_info_day():
    """smth"""
    day = request.form.get('day').split(" (")[0]
    day = datetime.strptime(day, "%a %b %d %Y %H:%M:%S GMT%z")

    user_id = session['logged_in_user_id']
    meals = Meal.query.filter(Meal.user_id == user_id, cast(Meal.date_time, Date) == day.date()).all()

    data = {'ingredient':[],
            'meal_type':[],
            'img':[]}
    for mil in meals:
        data['ingredient'].append(mil.meal_entry)
        data['meal_type'].append(mil.type_of_meal)
        data['img'].append(mil.img_url)

    return jsonify(data)
    


@app.route("/meal_journal_input", methods=["POST"])
def process_meal_journal_input():
    """Register user uploads to DB """

    user_id = session['logged_in_user_id']

    ingredients = request.form.get('ingredients')
    meal = request.form.get('meal_type')
    my_file = request.files['my_file']
    # print(ingredients, meal)
    # print("\n" * 5)

    result = cloudinary.uploader.upload(my_file,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_SECRET,
                                        cloud_name=CLOUD_NAME)

    img_url = result['secure_url']

    """Move to crud"""
    new_meal = Meal(
                user_id = user_id,
                meal_entry = ingredients,
                type_of_meal = meal,
                date_time = datetime.today(),
                img_url = img_url)

    db.session.add(new_meal)
    db.session.commit()

    
    user_id = session['logged_in_user_id']
    meals = Meal.query.filter(Meal.user_id == user_id).all()
    # data = {'ingredient':[],
    #         'meal_type':[],
    #         'img':[]}
    # for mil in meals:
    #     data['ingredient'].append(mil.meal_entry)
    #     data['meal_type'].append(mil.type_of_meal)
    #     data['img'].append(mil.img_url)

    
    # return redirect("/meal_journal")

    # return data

    return img_url

@app.route("/meal_journal")
def process_meals_preview():
    """Return Meal Page"""

    return render_template("meals.html")
    


#########################################################################
#                        Calendar                                       #
#########################################################################

@app.route("/calendar")
def show_calendar():
    """Return Calendar Page"""

    # notes = Notes.query.filter(Notes.user_id == user_id).all()
    
    # # notes_by_date = collections.defaultdict(list)
    # # for note in notes:
    # #     notes_by_date[(note.date_time.month, note.date_time.year)].append(note)

    # periods = Menstruation.query.filter(Menstruation.user_id == user_id, cast(Menstruation.period_start, Date) == date_time.date()).all()
    return render_template('all_calendar.html')


@app.route("/req_calendar", methods = ["POST"])
def req_calendar():
    """request data for current month in  Calendar Page"""

    user_id = session['logged_in_user_id']

    start_date = request.json.get('start_date').split("T")[0]
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = request.json.get('end_date').split("T")[0]
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    notes = Notes.query.filter(Notes.user_id == user_id, cast(Notes.date_time, Date) >= start_date, cast(Notes.date_time, Date) < end_date).all()
    periods = Menstruation.query.filter(Menstruation.user_id == user_id, cast(Menstruation.period_start, Date) >= start_date, cast(Menstruation.period_start, Date) < end_date).all()

    data = {'notes':[], 'periods':[]}
    
    for note in notes:
        i = int(note.date_time.split(' ')[0][-2:])
        if i not in data['notes']:
            data['notes'].append(i)
    for period in periods:
        i = int(period.period_start.split(' ')[0][-2:])
        if i not in data['periods']:
            data['periods'].append(i)

    return jsonify(data)




#########################################################################
#                       Period                                          #
#########################################################################

@app.route("/add_period.json", methods = ["POST"])
def add_period():
    """ adds period"""
    
    user_id = session['logged_in_user_id']

    
    p_length = int(request.json.get('period_length'))
    p_start = request.json.get('date_time').split('.')[0]
    p_start = datetime.strptime(p_start, "%Y-%m-%dT%H:%M:%S")

    
    """Move to crud"""
    for i in range(p_length):
        date = p_start + timedelta(days= i)
        new_period = Menstruation(
                    user_id = user_id,
                    period_start = date,
                    period_length = 1,
        )

        db.session.add(new_period)
    db.session.commit()


    return redirect("/calendar")

#########################################################################
#                       Note                                            #
#########################################################################

@app.route("/add_note.json", methods = ["POST"])
def add_note():
    """ adds note"""

    user_id = session['logged_in_user_id']

    note_t = request.json.get('note_text')
    date_time = request.json.get('date_time').split('.')[0]
    date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")

    # print("\n"*3)
    # print(date_time)
    # print("\n"*3)
    
    # print(note_text)
    # print("\n" * 5)


    """Move to crud"""
    new_note = Notes(
                user_id = user_id,
                notes_entry = note_t,
                date_time = date_time,
    )
    db.session.add(new_note)
    db.session.commit()


    return redirect("/calendar")

@app.route("/read_note.json", methods=["POST"])
def read_note():
    """ reads notes from database and returns back to js"""

    user_id = session['logged_in_user_id']

    date_time = request.json.get('note_date').split('.')[0]
    date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")

    notes = Notes.query.filter(Notes.user_id == user_id, cast(Notes.date_time, Date) == date_time.date()).all()
    data = {'notes':[]}

    for note in notes:
        data['notes'].append(note.notes_entry)


    return jsonify(data)

#########################################################################
#                       Stay Hydrated                                   #
#########################################################################

@app.route("/stay_hydrated", methods=["GET"])
def show_water_level():
    """Show water form."""
    return render_template("stay_hydrated.html")


@app.route("/enter_water", methods=["POST"])
def process_water():
    """Add user's hydration level to DB """

    hydration = float(request.json.get('hydration_level'))
    w_date = datetime.today().date()
    user_id = session['logged_in_user_id']
   
    
    """Move to crud"""
    new_water_entry = Water(
                        user_id = user_id,
                        water_entry = hydration,
                        date_time = w_date)
  
    db.session.add(new_water_entry)
    db.session.commit()


    return redirect('/get_water')


@app.route("/get_water")
def get_water():
    """request data for Water Page Images"""

    user_id = session['logged_in_user_id']
    water_goal =  Water.query.filter(Water.user_id == user_id, Water.water_entry==None).all()
    print(water_goal)
    if water_goal == []:
        water_goal = 3.
    else:
        water_goal = water_goal[-1].daily_water_goal
    hyd_levs =  Water.query.filter(Water.user_id == user_id, cast(Water.date_time, Date) == datetime.today().date(), Water.water_entry!=None).all()

    hyd_levs_sum = 0
    for lvl in hyd_levs:
        hyd_levs_sum += lvl.water_entry

    data = {'sum':hyd_levs_sum, 'water_goal':water_goal}
    return jsonify(data)


@app.route("/set_goal")
def set_goal():
    """set water goal"""
    user_id = session['logged_in_user_id']
    water_goal = request.args.get('water_goal')
    w_date = datetime.today().date()

    new_water_entry = Water(
                        user_id = user_id,
                        daily_water_goal = water_goal,
                        date_time = w_date)

    db.session.add(new_water_entry)
    db.session.commit()

    return redirect('/get_water')




#########################################################################
#                       USER REGISTER                                   #
#########################################################################


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
    if user:
        flash('An account with this email already exists')
        return redirect('/login')
    
    if password != confirm_password:
        flash('Password does not match, please try again')
        return redirect('/register')

    else:
        """Move to crud"""
        new_user = User(first_name = first_name,
                        last_name = last_name,
                        email = email,
                        password = password,
                        # profile_proto_url
                        created_at = datetime.today())
        
        db.session.add(new_user)
        db.session.commit()

        session['logged_in_user_id'] = new_user.user_id
        flash('Login successful')

    return redirect('/features')
        
#########################################################################
#                       USER LOGIN                                      #
#########################################################################


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