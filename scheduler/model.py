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
    

    def __repr__(self):
        return f'<User user_id={self.user_id} full_name={self.full_name} email={self.email}>'

class Appointment(db.Model):
    """Stores all the entries of appointments that are in the sustem"""
    __tablename__ = 'appoitments'

    appoitment_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    time = db.Column(db.Integer)
    date = db.Column(db.String, nullable = False)

    user = db.relationship('User', backref="appoitments")

    def __repr__(self):
        return f'<Appointment user_id={self.user_id} date={self.date} time={self.time} >'


# class Temperature(db.Model):
#     """Stores all the entries of temperature that are written for each user"""
#     __tablename__ = 'body_temperature'

#     temperature_entry_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True,
#                         unique=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     temperature_entry = db.Column(db.String(10), nullable=True)
#     temp_date = db.Column(db.String, nullable = False, default=datetime.today())

#     user = db.relationship('User', backref="body_temperature")

#     def __repr__(self):
#         return f'<Temp user_id={self.user_id} temperature_entry={self.temperature_entry} >'


def connect_to_db(flask_app, db_uri="postgresql:///scheduler", echo=True):
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