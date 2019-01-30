from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_db():

    # Local config
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}".format(
    #     user="postgres", pw="1qaz2wsx", host="jblin", port="5432", db="postgres") # Application config
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Silence the deprecation warning
    db = SQLAlchemy(app)
    # db.init_app(app)
    return db


def migrate_db(app, db):
    migrate = Migrate(app, db)
    return migrate
