"""Script to seed database."""

import os
from random import randint, choice
from datetime import datetime
import json

# import crud
import model
import server


os.system('dropdb fertility')
os.system('createdb fertility')


model.connect_to_db(server.app)
model.db.create_all()

with open('data/users_data.json') as f:
    meal_data = json.loads(f.read())

fnames = ["Olivia", "Emma", "Amelia", "Ava", "Sophia"]
lnames = ["Smith", "Johnson", "Williams", "Brown", "Jones"]

for n in range(1,2):
    email = 'mateshov@gmail.com'  # A unique email!
    password = '@3456789'
    fname = 'Olya'   #choice(fnames)
    lname = 'Mateshov'   #choice(lnames)

   # Creat a user
    new_user = model.User(first_name = fname,
                        last_name = lname,
                        email = email,
                        password = password,
                        created_at = datetime.today())

    model.db.session.add(new_user)

    temp_list = [96,97,96,97,96,97,96,97,96,97,96,97,]
    # Create temperature list
    for r in range(10):
        user_id = n
        temperature = temp_list[r]
        tdate = datetime(2022,4,1+r).date()

        new_temperature = model.Temperature(
                        user_id = user_id,
                        temperature_entry = float(temperature),
                        temp_date = tdate)
        model.db.session.add(new_temperature)
    
    # Create meal entries
    for meal in meal_data:
        meal_type = meal["meal_type"]
        img_url = meal["meal_path"]
        dt = datetime.strptime(meal["entry_date"], "%Y-%m-%d")
        # print(dt.date())
        ingredients = meal["ingredients"]

        new_meal = model.Meal(
                user_id = n,
                meal_entry = ingredients,
                type_of_meal = meal_type,
                date_time = dt.date(),
                img_url = img_url)

        model.db.session.add(new_meal)
    
    supp_dict = {"Vitamin C":[["with_breakfast", "1", "capsule"]], 
                "Vitamin D":[["mid_afternoon", "2", "capsule"], ["with_dinner", "2", "capsule"]], 
                "Tomorrow's Nutrition PRO Sunfiber":[["with_breakfast", "1", "scoop"]]}

    for supp in supp_dict.keys():
        for entry in supp_dict[supp]:
            supplement_time = entry[0]
            supplement_dose = entry[1]
            supplement_dose_type = entry[2]

            new_supplement = model.Supplement(
                                user_id = n,
                                supplement_entry = supp,
                                supplement_dose = supplement_dose,
                                supplement_dose_type = supplement_dose_type,
                                supplement_time = supplement_time)
                                # date_started = date_started

            model.db.session.add(new_supplement)

        

model.db.session.commit()


