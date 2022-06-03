from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from task import ToDo, ToDoList

app = Flask(__name__)
app.secret_key = 'dnjnjlksnxkx214sl'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(ToDo, '/ToDo/Today/<string:taskname>')
api.add_resource(ToDoList, '/ToDo/Today')
api.add_resource(UserRegister, '/register')
app.run(port=5000, debug= True) # debugger for development mode

