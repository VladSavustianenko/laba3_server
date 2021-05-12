import psycopg2
from flask import Flask
from flask_cors import CORS
import os

print(os.environ['HOST'])
con = psycopg2.connect(
    host=os.environ['HOST'],
    database=os.environ['DATABASE'],
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    port=os.environ['PORT']
)
cur = con.cursor()
target = 'https://chat-server-lab3.herokuapp.com/'

app = Flask(__name__)
CORS(app)


def close_connection():
    cur.close()
    con.close()

