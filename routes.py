from flask import jsonify, request, make_response
import time
import os
import config

from modules.avatar import Avatar
from modules.message import Message
from modules.person import Person
from modules.profile import Profile
from modules.session import Session

cur = config.cur
con = config.con
app = config.app


@app.route('/', methods=['GET', 'POST'])
def main():
    return jsonify('Main')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        user = Session.login_check(data[0], data[1])
        return make_response(
            {'id': user[0], 'token': user[1]}
        )
    else:
        return jsonify('Login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.json
        id = Person.get_users_count() + 1
        try:
            is_available = Person.unique_email_check(data[3])
            if is_available:
                Person.create(id, data[3], data[4])
                Profile.create(id, data[0], data[1], data[2])
                Avatar.create(id)
                return make_response(
                    {'isAvailable': True}
                )
            else:
                return make_response(
                    {'isAvailable': False}
                )
        except:
            con.commit()
            print("Failed add person")
    return jsonify('Sign up')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        token = request.json
        Session.logout(token)
    return jsonify('Log Out')


@app.route('/person', methods=['GET', 'POST'])
def person():
    if request.method == 'POST':
        token = request.json
        id = Session.token_check(token)
        if id:
            profile = Profile.get_profile(id)
            return make_response({
                'id': profile[0],
                'firstname': profile[1],
                'lastname': profile[2],
                'birth': profile[3],
                'picture': profile[4],
            })
        else:
            return make_response(
                {'id': id}
            )
    else:
        return jsonify('Person')


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        data = request.json
        Message.send_message(data[0], data[1], data[2], data[3])
    return jsonify(Message.get_messages())


@app.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        data = request.json
        Profile.edit_profile(data[0], data[1], data[2])
    return jsonify('Edit profile')


@app.route('/edit/id:<id>', methods=['GET', 'POST'])
def edit_picture(id):
    if request.method == 'POST':
        current_time = int(round(time.time() * 1000))
        picture = request.files[f'{id}:profilePicture']
        picture.save(os.path.join("static",
                                       f'{str(id)}.profilePictures.{str(current_time)}.{picture.filename}'))

        picture_url = f'{config.target}///static/{str(id)}.profilePictures.{str(current_time)}.{picture.filename}'
        Avatar.edit_profile_picture(id, picture_url)
    return jsonify('Edit profile picture')
