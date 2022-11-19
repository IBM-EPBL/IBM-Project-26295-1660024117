from app import db

class User(db.Model):
	""" This is the user """

	__tablename__ = "users"

	id = db.Column(db.Integer,  autoincrement=True, primary_key=True, nullable=False)
	username = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	password = db.Column(db.String(120), nullable=False)

	def __repr__(self):
		return '<User {}>'.format(self.username)

def connect_to_db(app, _database):
    """ Connect the database to our Flask app. """

    app.config['SQLALCHEMY_DATABASE_URI'] = _database
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)
