import config
import random

from modules.person import Person

cur = config.cur
con = config.con


class Session:
    @staticmethod
    def login_check(email, password):
        try:
            user = Person.login_check(email, password)
            if len(user):
                token = Session.generate_token()
                try:
                    cur.execute(
                        f"INSERT INTO Session VALUES ({user[0][0]}, '{token}')"
                    )
                    con.commit()
                except:
                    con.commit()
                    print("Couldn't insert token")
                return [user[0][0], token]
            else:
                return [0, '']
        except:
            con.commit()
            print("Couldn't find user")
            return [0, '']

    @staticmethod
    def logout(token):
        try:
            cur.execute(
                f"DELETE FROM Session "
                f"WHERE token = '{token}'"
            )
            con.commit()
        except:
            con.commit()
            print("Couldn't delete token")

    @staticmethod
    def token_check(token):
        try:
            cur.execute(
                f"SELECT id FROM Session "
                f"WHERE token = '{token}'"
            )
            id = cur.fetchall()
            if len(id):
                return id[0][0]
            else:
                return 0
        except:
            con.commit()
            print("Couldn't check token")
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
            # id = random.randint(0, 60)
            # print(symbols[60])
            token += symbols[random.randint(0, 60)]
        return token
