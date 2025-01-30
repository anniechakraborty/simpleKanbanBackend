from app.extensions import mongo

class User:
    @staticmethod
    def create_user(username, email, password_hash):
        user_object = {
            "username": username,
            "email": email,
            "password_hash": password_hash
        }
        mongo.db.users.insert_one(user_object)

    @staticmethod
    def find_by_username(username):
        print(username)

class Task:
    @staticmethod
    def create_task(title, description, user_id):
        task_data = {"title": title, "description": description, "user_id": user_id}
        print(task_data)

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
