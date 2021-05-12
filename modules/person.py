import config

cur = config.cur
con = config.con


class Person:
    @staticmethod
    def create(id, email, password):
        try:
            cur.execute(
                f"INSERT INTO Person VALUES({id}, '{email}', '{password}')"
            )
            con.commit()
        except:
            con.commit()
            print("Failed create person")

    @staticmethod
    def unique_email_check(email):
        try:
            cur.execute(
                f"SELECT COUNT(*) FROM Person "
                f"WHERE email = '{email}'"
            )
            return cur.fetchall()[0][0] == 0
        except:
            con.commit()
            print("Couldn't check email")
            return False

    @staticmethod
    def login_check(email, password):
        try:
            cur.execute(
                f"SELECT * FROM Person "
                f"WHERE email = '{email}' AND password = '{password}'"
            )
            return cur.fetchall()
        except:
            con.commit()
            print("Couldn't find person")
            return []

    @staticmethod
    def get_users_count():
        try:
            cur.execute(
                "SELECT COUNT(*) FROM Person "
            )
            return cur.fetchall()[0][0]
        except:
            con.commit()
            print("Couldn't get user's count")
            return 0
