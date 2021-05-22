import config
from create_db import *

db = config.db


class MessageService:
    @staticmethod
    def get_messages():
        messages = db.session.query(Message.id, Message.user_id, Message.text, Message.date, Message.time,
                                    Profile.name, Profile.surname, Avatar.url). \
            join(Profile, Profile.id == Message.user_id). \
            join(Avatar, Avatar.id == Profile.id).all()
        msg_data = []
        for message in messages:
            msg_data.append(list(message))
        return msg_data

    @staticmethod
    def send_message(user_id, text, date, time):
        id = MessageService.get_message_count() + 1
        insert = Message.__table__.insert().values(id=id, user_id=user_id, text=text, date=date, time=time)
        db.session.execute(insert)
        db.session.commit()

    @staticmethod
    def get_message_count():
        message_count = len(
            db.session.query(Message.id).all()
        )
        return message_count
