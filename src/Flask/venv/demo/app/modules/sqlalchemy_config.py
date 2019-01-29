from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app

db = SQLAlchemy()

DB_URI = "postgresql+psycopg2://{user}:{pw}@{server}/{db}".format(user="postgres",pw="1qaz2wsx",server="jblin",db="postgres")

def init_db():
    # Application config
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
    db = SQLAlchemy()
    db.init_app(app)



