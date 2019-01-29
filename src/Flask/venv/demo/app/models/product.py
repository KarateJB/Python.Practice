from modules.sqlalchemy_config import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, db.Sequence('products_id_seq'), primary_key=True)
    title = db.Column(db.String(200), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False, default=0)

    def __init__(self, title, price):
        self.title = title
        self.price = price