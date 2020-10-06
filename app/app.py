import os

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
import time
from flask_cors import CORS

import cpu
import ram

application = Flask(__name__)
CORS(application)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + \
    os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + \
    ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db

@application.route('/')
def index():
    return jsonify(
        status=True,
        message='API FUNCIONANDO / SERVIDOR A Y B'
    )

@application.route('/stats')
def stats():
    stats = {
        'cpu': cpu.get_cpu_percentage(),
        'ram': ram.get_ram_percentage(),
        'docs': db.todo.count()
    }

    return jsonify(
        status=True,
        stats=stats
    )

@application.route('/delete')
def getDelete():
    db.todo.delete_many({})

    return jsonify(
        status= True,
        message= 'ok'
    )

@application.route('/data')
def getData():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'author': todo['author'],
            'sentence': todo['sentence'],
            'time': todo['time'],
            'js_time': todo['js_time']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

@application.route('/data', methods=['POST'])
def createData():
    data = request.get_json(force=True)

    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    d = datetime.utcnow()
    for_js = int(time.mktime(d.timetuple())) * 1000

    item = {
        'author': data['author'],
        'sentence': data['sentence'],
        'time': current_time,
        'js_time': for_js
    }

    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='ok'
    ), 201


if __name__ == "__main__":
    print("INICIANDO API")
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT,
                    debug=ENVIRONMENT_DEBUG)
