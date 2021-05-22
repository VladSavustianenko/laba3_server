import config
from create_db import *

db = config.db


class PersonService:
    @staticmethod
    def create(id, email, password):
        insert = Person.__table__.insert().values(id=id, email=email, password=password)
        db.session.execute(insert)
        db.session.commit()

    @staticmethod
    def unique_email_check(email):
        person = db.session.query(Person.email).filter(Person.email == email).all()
        return len(person) == 0

    @staticmethod
    def login_check(email, password):
        user = db.session.query(Person.id, Person.email, Person.password). \
            filter(Person.email == email, Person.password == password).all()
        return user

    @staticmethod
    def get_users_count():
        users_count = len(
            db.session.query(Person.id).all()
        )
        return users_count
