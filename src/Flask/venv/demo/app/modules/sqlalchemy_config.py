from flask_sqlalchemy import SQLAlchemy
from common.db import db
from common.ma import ma


def init_db():
    db = SQLAlchemy()
    db.init_app(app)
    ma.init_app(app)
