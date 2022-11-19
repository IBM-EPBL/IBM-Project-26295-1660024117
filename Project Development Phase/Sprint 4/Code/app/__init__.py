import os
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import ibm_db_sa

ibm_db_sa.ibm_db.dialect.supports_statement_cache = True
# dialect().supports_statement_cache  = True

app = Flask(__name__)

_database = 'ibm_db_sa://bwz22240:21nFovCe3Kstj8SK@fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:32731/bludb;security=SSL;'

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = _database
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
db.app = app
db.init_app(app)


app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'petamailsender@gmail.com',
    MAIL_PASSWORD = 'petamail@123'
)
mail = Mail(app)


from app import routes