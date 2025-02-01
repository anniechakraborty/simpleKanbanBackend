from flask import Blueprint, request, jsonify
from app.wrappers import authorized
from app.tasks.utils import Message
from app.tasks.controllers import TaskController

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
@authorized
def get_all_tasks(logged_in_user):
    res = TaskController.get_tasks(logged_in_user)
    return res

@tasks_bp.route('/', methods=['POST'])
@authorized
def create_new_task(logged_in_user):
    data = request.get_json()
    res = TaskController.create_task(data, logged_in_user)
    return res

@tasks_bp.route('/<string:task_id>', methods=['GET'])
@authorized
def get_task(logged_in_user, task_id):
    res = TaskController.get_task_by_id(logged_in_user, task_id)
    return res


@tasks_bp.route('/<string:task_id>', methods=['PUT'])
@authorized
def update_existing_task(logged_in_user, task_id):
    print('Update existing task')

@tasks_bp.route('/<string:task_id>', methods=['DELETE'])
@authorized
def delete_existing_task(logged_in_user, task_id):
    print('Delete task')
