import config
import random
from create_db import *
from services.person import PersonService

db = config.db


class SessionService:
    @staticmethod
    def login_check(email, password):
        user = PersonService.login_check(email, password)
        if len(user):
            token = SessionService.generate_token()
            insert = Session.__table__.insert().values(id=user[0][0], token=token)
            db.session.execute(insert)
            db.session.commit()
            return [user[0][0], token]
        else:
            return [0, '']

    @staticmethod
    def logout(token):
        delete = Session.__table__.delete().where(Session.token == token)
        db.session.execute(delete)
        db.session.commit()

    @staticmethod
    def token_check(token):
        id = db.session.query(Session.id).filter(Session.token == token).one()
        if len(id):
            return id[0]
        else:
            return 0

    @staticmethod
    def generate_token():
        symbols = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
            'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        token = ''
        for i in range(40):
            token += symbols[random.randint(0, 60)]
        return token
