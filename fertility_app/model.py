"""Models for fertility app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()


class User(db.Model):
    """Stores information about each user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        unique=True)
    first_name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    profile_proto_url = db.Column(db.String(100), nullable = True, default = '/static/img/TBD_default-profile-photo.png')
    created_at = db.Column(db.DateTime)

    # body_temperature = a list of Items objects --> an attribute has been made for the Temperature Class
    # supplements = a list of Items objects --> an attribute has been made for the Supplement Class
    # meals = a list of Items objects --> an attribute has been made for the Meal Class

    def __repr__(self):
        return f'<User user_id={self.user_id} full_name={self.full_name} email={self.email}>'


class Temperature(db.Model):
    """Stores all the entries of temperature that are written for each user"""
    __tablename__ = 'body_temperature'

    temperature_entry_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    temperature_entry = db.Column(db.String(10), nullable=True)
    date_time = db.Column(db.String, nullable = False, default=datetime.today())

    user = db.relationship('User', backref="body_temperature")

    def __repr__(self):
        return f'<User user_id={self.user_id} temperature__entry={self.temperature__entry} >'


class Supplement(db.Model):
    """Stores all the entries of Supplements that are written for each user"""
    __tablename__ = 'supplements'

    supplement_entry_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    supplement_entry = db.Column(db.String(100), nullable=True)
    supplement_dose = db.Column(db.String(100), nullable=True)
    supplement_type = db.Column(db.String(100), nullable=True)
    date_time = db.Column(db.String, nullable = False, default=datetime.today())
    img_url = db.Column(db.String(10000), nullable=True, default = '/static/img/TBD_default-Supimage.png')

    user = db.relationship('User', backref="supplements")

    def __repr__(self):
        return f'<User user_id={self.user_id} supplement_entry={self.supplement_entry} >'

class Meal(db.Model):
    """Stores all the entries of meals that are written for each user"""
    __tablename__ = 'meals'

    meal__entry_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    meal_entry = db.Column(db.String(100), nullable=True)
    type_of_meal = db.Column(db.String(100), nullable=True)
    date_time = db.Column(db.String, nullable = False, default=datetime.today())
    img_url = db.Column(db.String(10000), nullable=True, default = '/static/img/TBD_default-mealimage.png')

    user = db.relationship('User', backref="meals")

    def __repr__(self):
        return f'<User user_id={self.user_id} meal_entry={self.meal_entry}>'

# class Water(db.Model):
#     """Stores all the entries of water that are written for each user"""

# class Menstruation(db.Model):
#     """Stores all the entries of menstruation that are written for each user"""

# class Notes(db.Model):
#     """Stores all the entries of text that are written for each user"""


def connect_to_db(flask_app, db_uri="postgresql:///fertility", echo=True):
    """Connests the database to the Flaskapp"""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    db.create_all()
    