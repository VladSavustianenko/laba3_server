import config

cur = config.cur
con = config.con


class Message:
    @staticmethod
    def get_messages():
        try:
            cur.execute(
                "SELECT Message.id, Message.user_id, Message.text, Message.date, Message.time, "
                "Profile.name, Profile.surname, Avatar.url "
                "FROM Message "
                "JOIN Profile ON Message.user_id = Profile.id "
                "JOIN Avatar ON Avatar.id = Profile.id"
            )
            return cur.fetchall()
        except:
            con.commit()
            print("Couldn't get message")
            return []

    @staticmethod
    def send_message(user_id, text, date, time):
        try:
            id = Message.get_message_count() + 1
            cur.execute(
                f"INSERT INTO Message VALUES("
                f"{id}, {user_id}, '{text}', '{date}', '{time}'"
                f")"
            )
            con.commit()
        except:
            con.commit()
            print("Couldn't send message")

    @staticmethod
    def get_message_count():
        try:
            cur.execute(
                "SELECT COUNT(*) FROM Message"
            )
            return cur.fetchall()[0][0]
        except:
            con.commit()
            print("Couldn't get message count")
