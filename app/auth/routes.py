from flask import Blueprint, request, jsonify
from app.auth.controllers import register_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    msg, status = register_user(data)
    if status == 400:
        return {
            'error': msg,
            'status' : status
        }
    else:
        return {
            "message": msg, 
            "status": status
        }

@auth_bp.route('/login', methods=['POST'])
def login():
    print('Login user')
