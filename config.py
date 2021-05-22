import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import proxy

target = proxy.TARGET

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{proxy.USER}:{proxy.PASSWORD}@{proxy.HOST}/{proxy.DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)

db = SQLAlchemy(app)
