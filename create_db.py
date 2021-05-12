import config

cur = config.cur
con = config.con


def create_user_table():
    try:
        cur.execute(
            f"CREATE TABLE Person "
            f"("
            f"id integer NOT NULL,"
            f"email character varying NOT NULL,"
            f"password character varying NOT NULL,"
            f"CONSTRAINT user_pkey PRIMARY KEY (id)"
            f")"
        )
        con.commit()
        print("Table User created!")
    except:
        con.commit()
        print("Table User already exist!")


def create_profile_table():
    try:
        cur.execute(
            f"CREATE TABLE Profile "
            f"("
            f"id integer NOT NULL,"
            f"name character varying NOT NULL,"
            f"surname character varying NOT NULL,"
            f"birth date,"
            f"CONSTRAINT profile_pkey PRIMARY KEY (id)"
            f")"
        )
        con.commit()
        print("Table Profile created!")
    except:
        con.commit()
        print("Table Profile already exist!")


def create_avatar_table():
    try:
        cur.execute(
            f"CREATE TABLE Avatar "
            f"("
            f"id integer NOT NULL,"
            f"url character varying, "
            f"CONSTRAINT avatar_pkey PRIMARY KEY (id)"
            f")"
        )
        con.commit()
        print("Table Avatar created!")
    except:
        con.commit()
        print("Table Avatar already exist!")


def create_message_table():
    try:
        cur.execute(
            f"CREATE TABLE Message "
            f"("
            f"id integer NOT NULL,"
            f"user_id integer NOT NULL,"
            f"text character varying NOT NULL,"
            f"date character varying,"
            f"time character varying,"
            f"CONSTRAINT message_pkey PRIMARY KEY (id)"
            f")"
        )
        con.commit()
        print("Table Message created!")
    except:
        con.commit()
        print("Table Message already exist!")


def create_session_table():
    try:
        cur.execute(
            f"CREATE TABLE Session "
            f"("
            f"id integer NOT NULL,"
            f"token character varying NOT NULL,"
            f"CONSTRAINT session_pkey PRIMARY KEY (token)"
            f")"
        )
        con.commit()
        print("Table Session created!")
    except:
        con.commit()
        print("Table Session already exist!")


def create():
    create_user_table()
    create_profile_table()
    create_avatar_table()
    create_message_table()
    create_session_table()
