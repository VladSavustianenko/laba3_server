import psycopg2
from flask import Flask
from flask_cors import CORS
import os


con = psycopg2.connect(
    host=os.environ['HOST'],
    database=os.environ['DATABASE'],
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    port=os.environ['PORT']
    # host='ec2-52-44-31-100.compute-1.amazonaws.com',
    # database='d1fqct9sb89al',
    # user='egsukzxripuiby',
    # password='26df186754bd4f578f5f684ca7cf855542ecace095f61d02a3d0d9556752ba49',
    # port=5432
)
cur = con.cursor()
target = 'https://chat-server-lab3.herokuapp.com/'

app = Flask(__name__)
CORS(app)


def close_connection():
    cur.close()
    con.close()

