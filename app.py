from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Creating a local db to store and retrieve tasks
tasks = [
    {
        'name' : 'College Project',
        'description': 'write a program for where one string is an anagram of another string.',
        'time': 17.30,
        'sub_task': [
            {
                'name': 'DSA',
                'content': 'Explain the data structure used for the the assignment.'
            }
        ]
    }
] 

# Example of how JavaScript is used for API endpoint testing
@app.route('/')
def home():
    return render_template('index.html')

# POST Create a Task /ToDo/Today/<string:taskname>
@app.route("/ToDo/Today", methods = ['POST'])
def create_task():
    request_data = request.get_json()
    new_task = {
        'name': request_data['name'],
        'description' : request_data['description'],
        'time' : request_data['time'],
        'sub_task': []
    }
    tasks.append(new_task)
    return jsonify(new_task)

# GET Single Task /ToDo/Today/<string:taskname>
@app.route('/ToDo/Today/<string:name>')
def get_task(name):
    for task in tasks:
        if task['name'] == name:
            return jsonify(task)
    return jsonify({'message': 'task not found'})

# GET List All Tasks /ToDo/Today
@app.route("/ToDo/Today")
def get_tasks():
    return jsonify({'tasks': tasks})

# POST Create subtask to a task /ToDo/Today/<string:taskname>/subtask
@app.route("/ToDo/Today/<string:name>/subtask", methods = ['POST'])
def create_subtask(name):
    request_data = request.get_json()
    for task in tasks:
        if task['name'] == name:
            new_sub_task = {
                'name': request_data['name'],
                'content': request_data['content']
            }
            task['sub_task'].append(new_sub_task)
            return jsonify(new_sub_task)
    return jsonify({'message': 'task not found'})



# PUT Edit or insert /ToDo/Today/<string:taskname>
# DELETE delete task /Todo/Today/<string:taskname>



app.run(port=5000)

