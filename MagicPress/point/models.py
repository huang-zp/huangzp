from datetime import datetime
from MagicPress import db


class Point(db.model):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    create_time = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    update_time = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    state = db.Column(db.Boolean, default=True)
    pic_path = db.Column(db.String(128))
    categories = db.relationship('Category', backref='picture')
    rate = db.Column(db.Float, default=0.00)
    true_time = db.Column(db.Integer)
    false_time = db.Column(db.Integer)

    def __repr__(self):
        return self.title


class DefinePoint(Point):
    abstract = db.Column(db.Text())


class CheckPoint(Point):
    true_answer = db.Column(db.String(128))
    false_answer = db.Column(db.String(128))


class ChoicePoint(Point):
    true_answer = db.Column(db.String(128))
    false_answer1 = db.Column(db.String(128))
    false_answer2 = db.Column(db.String(128))
    false_answer3 = db.Column(db.String(128))
