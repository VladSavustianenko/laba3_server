import config
from create_db import *

db = config.db


class AvatarService:
    @staticmethod
    def create(id):
        insert = Avatar.__table__.insert().values(id=id)
        db.session.execute(insert)
        db.session.commit()

    @staticmethod
    def edit_profile_picture(id, url):
        img = db.session.query(Avatar.url).filter(Avatar.id == id).all()
        if len(img):
            update = Avatar.__table__.update().where(Avatar.id == id).values(url=url)
            db.session.execute(update)
            db.session.commit()
        else:
            insert = Avatar.__table__.insert().values(id=id, url=url)
            db.session.execute(insert)
            db.session.commit()
