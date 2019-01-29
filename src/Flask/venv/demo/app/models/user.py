from modules.sqlalchemy_config import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, db.Sequence('users_id_seq'), primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=True)

    def __init__(self, name, phone, *args, **kwargs):
        self.name = name
        self.phone = phone

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


