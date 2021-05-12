import psycopg2
from flask import Flask
from flask_cors import CORS
import proxy

con = psycopg2.connect(
    host=proxy.HOST,
    database=proxy.DATABASE,
    user=proxy.USER,
    password=proxy.PASSWORD,
    port=proxy.PORT
)
cur = con.cursor()
target = proxy.TARGET

app = Flask(__name__)
CORS(app)


def close_connection():
    cur.close()
    con.close()

