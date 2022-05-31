from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required


from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'dnjnjlksnxkx214sl'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# Creating a local db to store and retrieve tasks
tasks = []

class ToDo(Resource):
    @jwt_required()
    def get(self, taskname):
        task = next(filter(lambda x: x['taskname']==taskname, tasks), None)  # using the lambda instead for for loop
        return {'task': task}, 200 if task else 404

    @jwt_required()
    def post(self, taskname):
        if next(filter(lambda x: x['taskname']==taskname, tasks), None):
            return {'message': 'A task with the name {} already exists'.format(taskname)}, 400 # if the task already exists, then return a message task already exists.
        data = request.get_json()
        task = {'taskname': taskname, 'time': data['time'], 'description': data['description']}
        tasks.append(task)
        return task, 201


class ToDoList(Resource):
    def get(self):
        return {'tasks': tasks}


api.add_resource(ToDo, '/ToDo/Today/<string:taskname>')
api.add_resource(ToDoList, '/ToDo/Today')
app.run(port=5000, debug= True) # debugger for development mode

