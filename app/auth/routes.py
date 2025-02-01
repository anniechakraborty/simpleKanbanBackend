from flask import Blueprint, request, jsonify
from app.auth.controllers import UserController

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    res = UserController.register_user(data)
    return res

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    res = UserController.login_user(data)
    return res

@auth_bp.route('/user', methods=['GET'])
def get_user():
    token = request.headers.get("Authorization").split(" ")[1]
    res = UserController.get_current_user(token)
    print(res)
    return res