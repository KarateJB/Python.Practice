from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB_URI = "postgresql+psycopg2://{user}:{pw}@{server}/{db}".format(user="postgres",pw="1qaz2wsx",server="jblin",db="postgres")
db = SQLAlchemy()

def init_db():
    # Application config
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
    db = SQLAlchemy(app)
    # db.init_app(app)
    return db

def migrate_db(app, db):
    migrate = Migrate(app, db)
    return migrate


