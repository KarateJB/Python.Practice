from flask_sqlalchemy import sqlalchemy as sc
from sqlalchemy_config import db

class User(db.Model):
    __tablename__ = "users"
    id = sc.Column(sc.Integer, sc.Sequence('users_id_seq'), primary_key=True)
    name = sc.Column(sc.String(50), unique=False, nullable=False)
    gender = sc.Column(sc.String(1), unique=False, nullable=False, type=sc.types.Boolean)
    phone = sc.Column(sc.String(20), unique=False, nullable=True)

    def __init__(self, name, gender, phone):
        self.name = name
        self.gender = gender
        self.phone = phone