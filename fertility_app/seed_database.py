"""Script to seed database."""

import os
from random import randint
from datetime import datetime

# import crud
import model
import server


os.system('dropdb fertility')
os.system('createdb fertility')


model.connect_to_db(server.app)
model.db.create_all()



for n in range(1,4):
    email = f'user{n}@test.com'  # A unique email!
    password = 'test'
    fname = f'user{n}'
    lname = f'user{n}ov'

   # Creat a user
    new_user = model.User(first_name = fname,
                        last_name = lname,
                        email = email,
                        password = password,
                        created_at = datetime.today())

    model.db.session.add(new_user)

    # Create temperature list
    for r in range(10):
        user_id = n
        temperature = randint(96,99)
        tdate = datetime(2022,4,1+r)

        new_temperature = model.Temperature(
                        user_id = user_id,
                        temperature_entry = float(temperature),
                        temp_date = tdate)
        model.db.session.add(new_temperature)

model.db.session.commit()


