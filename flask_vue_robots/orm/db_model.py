from . import db


class TBUser(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(32))


class Car(db.Model):
    __tablename__ = 'tf_car'
    __bind_key__ = 'db1'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32))


class Student(db.Model):
    __tablename__ = 'tb_student'
    __bind_key__ = 'db2'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(32))
