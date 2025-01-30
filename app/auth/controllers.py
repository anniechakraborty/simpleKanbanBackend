from flask import jsonify
from app.extensions import mongo, bcrypt, jwt, db
from app.auth.utils import Message
from flask_jwt_extended import create_access_token
from dotenv import load_dotenv
import datetime
import os

# Mongo connection established
usersCollection = db['users']

def register_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Checking for blank fields and exisiting users
    if not username or not password or not email:
        return Message.MISSING_DETAILS, 400

    existing_user = usersCollection.find_one({"username": username})
    if existing_user:
        return Message.DUPLICATE_USER, 400
    
    exisitng_email = usersCollection.find_one({"email": email})
    if exisitng_email:
        return Message.DUPLICATE_EMAIL, 400

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    user_object = {
        "username": username,
        "email": email,
        "password_hash": password_hash,
        "created_at": datetime.datetime.now()
    }
    result = usersCollection.insert_one(user_object)
    print(result)

    return Message.USER_REGISTERED, 201
