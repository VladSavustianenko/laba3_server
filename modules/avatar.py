import config

cur = config.cur
con = config.con


class Avatar:
    @staticmethod
    def create(id):
        try:
            cur.execute(
                f"INSERT INTO Avatar(id) VALUES({id})"
            )
            con.commit()
        except:
            con.commit()
            print("Failed create avatar")

    @staticmethod
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
