"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

# import crud
import model
import server


os.system('dropdb fertility')
os.system('createdb fertility')


model.connect_to_db(server.app)
model.db.create_all()


with open('data/fertility.json') as f:
    fertility_data = json.loads(f.read())


fertility_list = []
for fertility in fertility_data:
    dt = datetime.strptime(fertility['release_date'], "%Y-%m-%d")
    fertility_list.append(crud.create_fertility(fertility['title'], fertility['overview'], dt, movie['poster_path']))


model.db.session.add_all(fertility_list)
model.db.session.commit()


for n in range(10):
    email = f'user{n}@test.com'  # A unique email!
    password = 'test'

   # Creat a user
    db_user = crud.create_user(email, password)
    model.db.session.add(db_user)
    # Create temperature list
    for r in range(10):
        m = choice(movie_list)
        ratin = crud.create_rating(db_user, m, randint(1,5))
        model.db.session.add(ratin)
model.db.session.commit()


