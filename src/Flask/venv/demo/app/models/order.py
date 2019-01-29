from modules.sqlalchemy_config import db


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, db.Sequence('orders_id_seq'), primary_key=True)
    count = db.Column(db.Integer, unique=False, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    def __init__(self, count, user_id, product_id):
        self.count = count
        self.user_id = user_id
        self.product_id = product_id
