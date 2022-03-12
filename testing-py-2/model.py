from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
   
    game2 = Game(name="SpotIt", description="Macthing images game")
    game3 = Game(name="Battleship", description="Destroy your enemys ship")
    

    db.session.add(game2)
    db.session.add(game3)
    db.session.commit()
    


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
