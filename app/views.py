from flask import Blueprint
from flask import request
from .responses import response
from .responses import not_found
from .responses import bad_request
from .models.task import Task

# endpoint handling
api_v1 = Blueprint("api",__name__, url_prefix='/api/v1')

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    # paginator
    page = int(request.args.get('page', 1)) # default value 1
    order = int(request.args.get('order', 'desc')) # sorting
    tasks = Task.get_by_page(order,page)
    # tasks = Task.query.all() # brings all tasks
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
    # forcing JSON response
    json = request.get_json(force=True)
    if json.get('title') is None or len(json.get('title')) > 50:
        return bad_request()

    if json.get('description') is None:
        return bad_request()

    if json.get('deadline') is None:
        return bad_request()

    # adding new task
    task = Task.new(json['title'], json['description'], json['deadline'])
    # return boolean from instance class method save
    if task.save():
        return response(task.serialize())

    return bad_request()

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.filter_by(id=id).first()
    if task is None:
        return not_found()

    json = request.get_json(force=True)
    task.title = json.get('title', task.title)
    task.description = json.get('description', task.description)
    task.deadline = json.get('deadline', task.deadline)

    if task.save():
        return response(task.serialize())
    else:
        return bad_request()

@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    if task is None:
        return not_found()

    if task.delete():
        # is deleted (but persistest for the response)
        return response(task.serialize())
    else:
        return bad_request()
