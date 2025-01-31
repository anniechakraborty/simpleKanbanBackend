import jwt
import datetime
from app.config import jwt_secret_key

class Message:
    DUPLICATE_USER = "User already exists!"
    DUPLICATE_EMAIL = "User already exists with this email address!"
    INVALID_DETAILS = 'Invalid username or password!'

    MISSING_DETAILS = 'Username, email and password required'

    USER_REGISTERED = 'User registered successfully!'
    USER_LOGGED_IN = 'User logged in successfully!'
    USER_LOGGED_OUT = 'User logged out successfully!'

class TokenManagement:
    def generate_access_token(identity):
        jwt_payload = {
            'user_id': identity,
            'exp': datetime.datetime.now() + datetime.timedelta(days=1)
        }
        jwt_algorithm = "HS256"
        return jwt.encode(jwt_payload, jwt_secret_key, algorithm=jwt_algorithm)