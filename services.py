import random
import config

cur = config.cur
con = config.con


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


def get_users():
    try:
        cur.execute(
            "SELECT * FROM Person "
        )
        return cur.fetchall()
    except:
        con.commit()
        print("Couldn't get users")


def get_profile(id):
    # try:
        cur.execute(
            f"SELECT Profile.id, Profile.name, Profile.surname, Profile.birth, Avatar.url FROM Profile "
            f"JOIN Avatar ON Avatar.id = Profile.id "
            f"WHERE Profile.id = {id}"
        )
        return cur.fetchall()[0]
    # except:
    #     con.commit()
    #     print("Couldn't get profile")


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


def login_check(data):
    try:
        cur.execute(
            f"SELECT * FROM Person "
            f"WHERE email = '{data[0]}' AND password = '{data[1]}'"
        )
        user = cur.fetchall()
        if len(user):
            token = generate_token()
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


def get_message_count():
    try:
        cur.execute(
            "SELECT COUNT(*) FROM Message"
        )
        return cur.fetchall()[0][0]
    except:
        con.commit()
        print("Couldn't get message count")


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


def send_message(message):
    try:
        id = get_message_count() + 1
        cur.execute(
            f"INSERT INTO Message VALUES("
            f"{id}, {message[0]}, '{message[1]}', '{message[2]}', '{message[3]}'"
            f")"
        )
        con.commit()
    except:
        con.commit()
        print("Couldn't send message")


def edit_profile(data):
    try:
        cur.execute(
            f"UPDATE Profile "
            f"SET name = '{data[1]}', surname = '{data[2]}' WHERE id = {data[0]}"
        )
        con.commit()
    except:
        con.commit()
        print("Couldn't update profile")


def edit_profile_picture(id, url):
    try:
        try:
            cur.execute(
                f"INSERT INTO Avatar VALUES({id}, '{url}')"
            )
            con.commit()
        except:
            con.commit()
            cur.execute(
                f"UPDATE Avatar "
                f"SET url = '{url}' WHERE id = {id}"
            )
            con.commit()
    except:
        con.commit()
        print("Couldn't add picture")
