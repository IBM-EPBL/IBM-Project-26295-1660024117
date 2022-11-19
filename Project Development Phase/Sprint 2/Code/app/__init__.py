import os
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy()

_database = 'ibm_db_sa://<uid>:<pass>@<hostname>:<port>/bludb;security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt'

from app.models import connect_to_db
connect_to_db(app,_database)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = '<email_id>',
    MAIL_PASSWORD = '<password>'
)
mail = Mail(app)


from app import routes