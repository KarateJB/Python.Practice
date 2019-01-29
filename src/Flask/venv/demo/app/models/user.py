from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from modules.sqlalchemy_config import db

class User(db.Model):
    __tablename__ = "Users"
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('user_id_seq'), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50), unique=False, nullable=False)
    gender = sqlalchemy.Column(sqlalchemy.String(1), unique=False, nullable=False, type=sqlalchemy.types.Boolean)
    phone = sqlalchemy.Column(sqlalchemy.String(20), unique=False, nullable=True)    