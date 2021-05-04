from flask import Flask, jsonify, request, make_response, session, g, redirect, url_for

import psycopg2

import routes
import create_db
import config


app = config.app


if __name__ == '__main__':
    print("Hello!!")
    create_db.create()
    app.run(debug="True")


config.close_connection()

