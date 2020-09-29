import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import psutil

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db

psutil.cpu_percent(interval=None)

@application.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

@application.route('/todo')
def todo():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

@application.route('/stats')
def todo():

    stats = {
        'cpu_freq_percpu': psutil.cpu_freq(percpu=True),
        'cpu_freq': psutil.cpu_freq(percpu=True),
        'cpu_stats': psutil.cpu_stats(),
        'cpu_count_logical': psutil.cpu_count(),
        'cpu_count_physical': psutil.cpu_count(logical=False),
        'cpu_times_percent': psutil.cpu_times_percent(1, False),
        'cpu_times_percent_percpu': psutil.cpu_times_percent(1, True),
        'cpu_percent': psutil.cpu_percent(interval=None),
        'cpu_percent_percpu': psutil.cpu_percent(interval=None, percpu=True),
        'memory': psutil.virtual_memory()
    }

    return jsonify(
        status=True,
        stats=stats
    )

@application.route('/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)