from datetime import datetime
from bson import ObjectId
from app.config import db
from app.tasks.utils import Message

tasksCollection = db['tasks']
class TaskController:
    def create_task(data, user):
        print(data)
        task_obj = {
            'title': data['title'],
            'description': data['description'],
            'status': data['status'],
            'created_by': user['username'],
            'created_on': datetime.now()
        }
        try:
            result = tasksCollection.insert_one(task_obj)
            if result:
                return {
                    'message': Message.CREATE_TASK, 
                    'taskId': str(result.inserted_id),
                    'status': 200
                }
            else:
                return {'message': Message.ERROR_IN_CREATE_TASK, 'status': 500}
        except Exception as e:
            return {'message': str(e), 'status': 500}

    def get_tasks(user):
        try:
            tasks = tasksCollection.find({'created_by': user['username']})
            if tasks:
                res = {
                    'task': [],
                    'status': 200
                }
                for task in tasks:
                    task['_id'] = str(task['_id'])
                    res['task'].append(task)
                return res
            else:
                return {
                    'message': Message.TASK_NOT_FOUND,
                    'tasks': [],
                    'status': 200
                }
        except Exception as e:
            return {'message': str(e), 'status': 500}
    
    def get_task_by_id(user, task_id):
        try:
            task = tasksCollection.find_one({'_id': ObjectId(task_id), 'created_by': user['username']})
            print(task)
            print(type(task))
            if task:
                task['_id'] = str(task['_id'])
                return {
                    'task': task,
                    'status': 200
                }
            else:
                return {
                    'message': Message.TASK_NOT_FOUND,
                    'task': None,
                    'status': 404
                }
        except Exception as e:
            return {'message': str(e), 'status': 500}
    
    def update_task(user, task_id, data):
        print(user, task_id, data)
        try:
            updated_task = tasksCollection.update_one(
                {'_id': ObjectId(task_id), 'created_by': user['username']}, 
                {'$set': data}
            )
            if updated_task.modified_count > 0:
                return {
                    'message': Message.UPDATE_TASK,
                    'status': 200
                }
            else:
                return {
                    'message': Message.TASK_NOT_FOUND,
                    'status': 404
                }
        except Exception as e:
            return {'message': str(e), 'status': 500}
    
    def delete_task(user, task_id):
        print(user, task_id)
        try:
            deleted_task = tasksCollection.delete_one({'_id': ObjectId(task_id), 'created_by': user['username']})
            if deleted_task.deleted_count > 0:
                return {
                    'message': Message.DELETE_TASK,
                    'status': 200
                }
            else:
                return {
                    'message': Message.TASK_NOT_FOUND,
                    'status': 404
                }
        except Exception as e:
            return {'message': str(e), 'status': 500}