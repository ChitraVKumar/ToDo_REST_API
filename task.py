from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from datetime import datetime

class ToDo(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('time', type=lambda s: str(datetime.datetime.strptime(s,"%d/%m/%Y %H:%M:%S")), required= True, help='Required!')
    parser.add_argument('description', type=str, required = True, help='Required')


    @jwt_required()
    def get(self, taskname):
        task = next(filter(lambda x: x['taskname']==taskname, tasks), None)  # using the lambda instead for for loop
        return {'task': task}, 200 if task else 404

    @jwt_required()
    def post(self, taskname):

        if next(filter(lambda x: x['taskname']==taskname, tasks), None):
            return {'message': 'A task with the name {} already exists'.format(taskname)}, 400 # if the task already exists, then return a message task already exists.

        data = ToDo.parser.parse_args()
        
        task = {'taskname': taskname, 'time': data['time'], 'description': data['description']}
        tasks.append(task)
        return task, 201

    @jwt_required()
    def delete(self, taskname):
        global tasks
        tasks = list(filter(lambda x: x['taskname'] != taskname, tasks))
        return {'message': 'Task deleted'}

    @jwt_required()
    def put(self, taskname):
        data = ToDo.parser.parse_args()

        task = next(filter(lambda x: x['taskname'] == taskname, tasks), None)
        if task is None:
            task = {'taskname': taskname, 'description': data['description'], 'time': data['time']}
            tasks.append(task)
        else:
            task.update(data)

        return task


class ToDoList(Resource):
    @jwt_required()
    def get(self):
        return {'tasks': tasks}