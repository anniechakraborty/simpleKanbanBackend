from flask import jsonify
from app.extensions import bcrypt, jwt_secret_key, db
from app.auth.utils import Message
import datetime
import jwt

# Mongo connection established
usersCollection = db['users']

def register_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Checking for blank fields and exisiting users
    if not username or not password or not email:
        response = {
            'error': Message.MISSING_DETAILS,
            'status': 400
        }
        return response

    existing_user = usersCollection.find_one({"username": username})
    if existing_user:
        response = {
            'error': Message.DUPLICATE_USER,
            'status': 400
        }
        return response
    
    exisitng_email = usersCollection.find_one({"email": email})
    if exisitng_email:
        response = {
            'error': Message.DUPLICATE_EMAIL,
            'status': 400
        }
        return response

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    user_object = {
        "username": username,
        "email": email,
        "password_hash": password_hash,
        "created_at": datetime.datetime.now()
    }
    result = usersCollection.insert_one(user_object)
    print('USERS REGISTERED ! ', result)
    response = {
        'message': Message.USER_REGISTERED,
        'data': 1,
        'status': 200
    }
    return response

def login_user(data):
    email = data.get('email')
    password = data.get('password')

    user = usersCollection.find_one({"email": email})
    
    if not user or not bcrypt.check_password_hash(user['password_hash'], password):
        response = {
            'error': Message.INVALID_DETAILS,
            'status': 401
        }
        return response
    
    # Generate a JWT token
    jwt_payload = {
        'user_id': str(user['_id']),
        'exp': datetime.datetime.now() + datetime.timedelta(days=1)
    }
    jwt_algorithm = "HS256"
    access_token = jwt.encode(jwt_payload, jwt_secret_key, algorithm=jwt_algorithm)

    # access_token = create_access_token(identity=str(user['_id']), expires_delta=datetime.timedelta(hours=24))
    response = {
        'message': Message.USER_LOGGED_IN,
        'access_token': access_token,
        'status': 200
    }
    return response

def validate_token(token):
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
