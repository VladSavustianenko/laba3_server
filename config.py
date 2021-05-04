import psycopg2
from flask import Flask
from flask_cors import CORS


con = psycopg2.connect(
    database="laba3",
    user="postgres",
    password="admin"
)
cur = con.cursor()
new_db_name = "laba3"
target = 'http://localhost:5000'

app = Flask(__name__)
CORS(app)


def close_connection():
    cur.close()
    con.close()

