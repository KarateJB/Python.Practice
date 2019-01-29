from flask_sqlalchemy import sqlalchemy as sc
from sqlalchemy_config import db

class Order(db.Model):
    __tablename__ = "orders"
    id = sc.Column(sc.Integer, sc.Sequence('orders_id_seq'), primary_key=True)
    count = sc.Column(sc.Integer, unique=False, default=1)
    user_id = sc.Column(sc.Integer, sc.ForeignKey('user.id'), nullable=False)
    product_id = sc.Column(sc.Integer, sc.ForeignKey('product.id'), nullable=False)

    def __init__(self, count, user_id, product_id):
        self.count = count
        self.user_id = user_id
        self.product_id = product_id
