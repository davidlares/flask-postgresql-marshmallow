from flask import Blueprint
from .responses import response
from .responses import not_found
from .models.task import Task

# endpoint handling
api_v1 = Blueprint("api",__name__, url_prefix='/api/v1')

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all() # brings all tasks
    # using list comprenhensions for serialize each item
    return response([task.serialize() for task in tasks])

@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    # filtering by id
    task = Task.query.filter_by(id=id).first()
    if task is None:
        return not_found()
    return response(task.serialize())

@api_v1.route('/tasks', methods=['POST'])
def create_task():
    pass

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    pass

@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task():
    pass
