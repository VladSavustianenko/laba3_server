import config

db = config.db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    surname = db.Column(db.String, nullable=True)
    birth = db.Column(db.String)


class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    text = db.Column(db.String, nullable=True)
    date = db.Column(db.String)
    time = db.Column(db.String)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=True)


def create():
    db.create_all()
