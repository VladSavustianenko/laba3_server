import config

cur = config.cur
con = config.con


class Profile:
    @staticmethod
    def create(id, name, surname, birth):
        try:
            cur.execute(
                f"INSERT INTO Profile VALUES({id}, '{name}', '{surname}', '{birth}')"
            )
            con.commit()
        except:
            con.commit()
            print("Failed create profile")

    @staticmethod
    def get_profile(id):
        try:
            cur.execute(
                f"SELECT Profile.id, Profile.name, Profile.surname, Profile.birth, Avatar.url FROM Profile "
                f"JOIN Avatar ON Avatar.id = Profile.id "
                f"WHERE Profile.id = {id}"
            )
            return cur.fetchall()[0]
        except:
            con.commit()
            print("Couldn't get profile")

    @staticmethod
    def edit_profile(id, name, surname):
        try:
            cur.execute(
                f"UPDATE Profile "
                f"SET name = '{name}', surname = '{surname}' WHERE id = {id}"
            )
            con.commit()
        except:
            con.commit()
            print("Couldn't update profile")
