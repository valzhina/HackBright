"""Script to seed database."""

import os

import model
import server


os.system('dropdb scheduler')
os.system('createdb scheduler')


model.connect_to_db(server.app)
model.db.create_all()


email = 'mateshov@gmail.com'  # A unique email!
password = '@3456789'
fname = 'Olya'   #choice(fnames)
lname = 'Mateshov'   #choice(lnames)

# Creat a user
new_user = model.User(first_name = fname,
                    last_name = lname,
                    email = email,
                    password = password)

model.db.session.add(new_user)

for t in [10, 14, 17]:
    new_app = model.Appointment(user_id = 1,
                                time = t,
                                date = "2022-04-29")
    
    model.db.session.add(new_app)


model.db.session.commit()