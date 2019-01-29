from flask_sqlalchemy import SQLAlchemy
from modules.sqlalchemy_config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    gender = db.Column(db..String(50), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=True)    