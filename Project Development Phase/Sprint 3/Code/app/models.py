from app import db

class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer,  autoincrement=True, primary_key=True, nullable=False)
	username = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	password = db.Column(db.String(120), nullable=False)

	def __repr__(self):
		return '<User {}>'.format(self.username)


class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(db.String(64))
    category_daily = db.Column(db.Boolean, default=False)  # is it daily expense related, False implies, it can be both daily and monthly!?
    category_primary =  db.Column(db.Boolean, default=False)  # if not true, it means , this category is added explicitly by user!


class Budget(db.Model):

    __tablename__ = "budget"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    budget_amount = db.Column(db.Numeric(15, 2))
    budget_userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    budget_month = db.Column(db.Integer) 
    budget_year = db.Column(db.Integer)

    user = db.relationship("User", backref=db.backref('budget'))

    def __repr__(self):

        return "<Budget id=%s budget=%s budget_userid=%s budget_month=%s budget_year=%s>" % (
            self.id, self.budget_amount, self.budget_userid, self.budget_month, self.budget_year)


class Expenditure(db.Model):

    __tablename__ = "expenditures"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    spent = db.Column(db.Numeric(15, 2), default=0)
    date_of_expenditure = db.Column(db.DateTime)
    expenditure_userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    where_spent = db.Column(db.String(100))
    description = db.Column(db.UnicodeText)

    user = db.relationship("User", backref=db.backref('expenditures'))

    category = db.relationship("Category", backref=db.backref('expenditures'))


def connect_to_db(app, _database):

    app.config['SQLALCHEMY_DATABASE_URI'] = _database
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)
