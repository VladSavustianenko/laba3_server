import config
from create_db import *

db = config.db


class ProfileService:
    @staticmethod
    def create(id, name, surname, birth):
        insert = Profile.__table__.insert().values(id=id, name=name, surname=surname, birth=birth)
        db.session.execute(insert)
        db.session.commit()

    @staticmethod
    def get_profile(id):
        profile = db.session.query(Profile.id, Profile.name, Profile.surname, Profile.birth, Avatar.url). \
            join(Avatar, Avatar.id == Profile.id). \
            where(Profile.id == id).one()
        return profile

    @staticmethod
    def edit_profile(id, name, surname):
        update = Profile.__table__.update().where(Profile.id == id).values(name=name, surname=surname)
        db.session.execute(update)
        db.session.commit()
