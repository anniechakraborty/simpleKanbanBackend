from app.config import db

class User:
    collection = db['users']
    @staticmethod
    def create_user(user_object):
        User.collection.insert_one(user_object)

    @staticmethod
    def find_by_username(username):
        User.collection.find({'username': username})

class Task:
    collection = db['tasks']
    @staticmethod
    def create_task(task_data):
        print(task_data)
        Task.collection.insert_one(task_data)

    @staticmethod
    def get_tasks_by_user(user_id):
        print(user_id)

    @staticmethod
    def update_task(task_id, updates):
        print(task_id)
        print(updates)

    @staticmethod
    def delete_task(task_id):
        print(task_id)
