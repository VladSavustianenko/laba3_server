import psycopg2
from flask import Flask
from flask_cors import CORS
import os


con = psycopg2.connect(
    host=os.environ.get("HOST"),
    database=os.environ.get("DATABASE"),
    user=os.environ.get("USER"),
    password=os.environ.get("PASSWORD"),
    port=os.environ.get("PORT")
)
cur = con.cursor()
target = 'https://chat-server-lab3.herokuapp.com/'

app = Flask(__name__)
CORS(app)


def close_connection():
    cur.close()
    con.close()

