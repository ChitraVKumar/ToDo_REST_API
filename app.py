from datetime import datetime
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import datetime


from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'dnjnjlksnxkx214sl'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# Creating a local db to store and retrieve tasks
tasks = []

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


api.add_resource(ToDo, '/ToDo/Today/<string:taskname>')
api.add_resource(ToDoList, '/ToDo/Today')
api.add_resource(UserRegister, '/register')
app.run(port=5000, debug= True) # debugger for development mode

