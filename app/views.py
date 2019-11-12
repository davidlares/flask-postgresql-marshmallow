from flask import request
from flask import Blueprint

from .models.task import Task
from .responses import response
from .responses import not_found
from .responses import bad_request

from .schemas import task_schema
from .schemas import tasks_schema
from .schemas import params_task_schema

# endpoint handling
api_v1 = Blueprint("api",__name__, url_prefix='/api/v1')

# decorator
def set_task(function):
    # nested function
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        task = Task.query.filter_by(id=id).first()
        if task is None:
            return not_found()
        # retuning the decorator with the task
        return function(task)
        # renaming the function for multiple uses
    wrap.__name__ = function.__name__
    return wrap


@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    # paginator
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    tasks = Task.get_by_page(order, page)
    # tasks = Task.query.all() # brings all tasks
    # using list comprenhensions for serialize each item
    # return response([task.serialize() for task in tasks])
    return response(tasks_schema.dump(tasks))

@api_v1.route('/tasks/<id>', methods=['GET'])
@set_task
def get_task(task):
    # filtering by id
    # return response(task.serialize())
    return response(task_schema.dump(task))

@api_v1.route('/tasks', methods=['POST'])
def create_task():
    # forcing JSON response
    json = request.get_json(force=True)
    # if json.get('title') is None or len(json.get('title')) > 50:
    #     return bad_request()
    #
    # if json.get('description') is None:
    #     return bad_request()
    #
    # if json.get('deadline') is None:
    #     return bad_request()

    error = params_task_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    # adding new task
    task = Task.new(json['title'], json['description'], json['deadline'])
    # return boolean from instance class method save
    if task.save():
        # return response(task.serialize())
        return response(task_schema.dump(task))
    return bad_request()

@api_v1.route('/tasks/<id>', methods=['PUT'])
@set_task
def update_task(task):
    json = request.get_json(force=True)
    task.title = json.get('title', task.title)
    task.description = json.get('description', task.description)
    task.deadline = json.get('deadline', task.deadline)
    if task.save():
        # return response(task.serialize())
        return response(task_schema.dump(task))
    return bad_request()

@api_v1.route('/tasks/<id>', methods=['DELETE'])
@set_task
def delete_task(task):
    if task.delete():
        # is deleted (but persistest for the response)
        # return response(task.serialize())
        return response(task_schema.dump(task))
    return bad_request()
