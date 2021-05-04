from flask import Flask, jsonify, request, make_response, session, g, redirect, url_for

import psycopg2

import routes
import create_db
import config

cur = config.cur
con = config.con
app = config.app


if __name__ == '__main__':
    create_db.create()
    app.run(debug="True")


# config.close_connection()

