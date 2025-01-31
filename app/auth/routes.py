from flask import Blueprint, request, jsonify
from app.auth.controllers import register_user, login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    res = register_user(data)
    return res

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    res = login_user(data)
    return res
