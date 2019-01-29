from flask_sqlalchemy import sqlalchemy as sc
from sqlalchemy_config import db

class Product(db.Model):
    __tablename__ = "products"
    id = sc.Column(sc.Integer, sc.Sequence('products_id_seq'), primary_key=True)
    title = sc.Column(sc.String(200), unique=False, nullable=False)
    price = sc.Column(sc.Integer, unique=False, nullable=False, default=0)

    def __init__(self, title, price):
        self.title = title
        self.price = price