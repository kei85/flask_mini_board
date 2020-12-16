from datetime import datetime
from flask_app import db, ma

class Board(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(255, convert_unicode=True), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

def find_all():
    boards = Board.query.order_by(Board.created_at.desc()).all()
    return boards

def find_one(id):
    boards = db.session.query(Board).filter(Board.uid == id).all()
    return boards

def create(data, id):
    brd = Board()
    brd.uid = id
    brd.message = data["message"]

    db.session.add(brd)
    db.session.commit()


class BoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Board