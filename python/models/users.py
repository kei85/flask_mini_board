from datetime import datetime
from flask_app import db, ma

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255, convert_unicode=True), nullable=False)
    pwd = db.Column(db.String(255, convert_unicode=True), nullable=False)
    mail = db.Column(db.String(255, convert_unicode=True), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    pwd = ma.auto_field()
    mail = ma.auto_field()
    age = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()


def create(data):
    usr = User()
    usr.name = data["name"]
    usr.pwd = data["pwd"]
    usr.mail = data["mail"]
    usr.age = data["age"]

    db.session.add(usr)
    db.session.commit()

def update(data, id):
    usr = db.session.query(User).filter(User.id == id).first()

    usr.name = data["name"]
    usr.mail = data["mail"]
    usr.pwd = data["pwd"]
    usr.age = data["age"]

    db.session.add(usr)
    db.session.commit()

def find_user(id):
    usr = db.session.query(User).filter(User.id == id).first()
    return usr