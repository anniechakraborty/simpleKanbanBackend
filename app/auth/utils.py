import jwt
import datetime
from app.config import jwt_secret_key

class Message:
    DUPLICATE_USER = "User already exists!"
    DUPLICATE_EMAIL = "User already exists with this email address!"
    INVALID_DETAILS = 'Invalid username or password!'

    MISSING_DETAILS = 'Username, email and password required'
    MISSING_TOKEN = 'Authentication is required!'
    
    USER_NOT_FOUND = 'User not found!'
    USER_UNAUTHENTICATED = 'User is not authorized!'

    USER_FOUND = 'User exists!'
    USER_REGISTERED = 'User registered successfully!'
    USER_LOGGED_IN = 'User logged in successfully!'
    USER_LOGGED_OUT = 'User logged out successfully!'

    TOKEN_EXPIRED = 'Token has expired!'
    TOKEN_INVALID = 'Token is invalid!'

class TokenManagement:
    def generate_access_token(identity):
        jwt_payload = {
            'user_id': identity,
            'exp': datetime.datetime.now() + datetime.timedelta(days=1)
        }
        jwt_algorithm = "HS256"
        return jwt.encode(jwt_payload, jwt_secret_key, algorithm=jwt_algorithm)
    
    def decode_token(token):
        return jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
    
    def validate_token(token):
        try:
            payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return Message.TOKEN_EXPIRED
        except jwt.InvalidTokenError:
            return Message.TOKEN_INVALID
            