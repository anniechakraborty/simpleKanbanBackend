from flask import Blueprint, request, jsonify

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
def get_all_tasks():
    print('Get all tasks')

@tasks_bp.route('/', methods=['POST'])
def create_new_task():
    print('Create new task')

@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_existing_task(task_id):
    print('Update existing task')

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_existing_task(task_id):
    print('Delete task')
