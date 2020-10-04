import os

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import psutil
from datetime import datetime

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db

psutil.cpu_percent(interval=None)

@application.route('/')
def index():
    return jsonify(
        status=True,
        message='API FUNCIONANDO / SERVIDOR A Y B'
    )

@application.route('/stats')
def stats():
    memory = psutil.virtual_memory()

    THRESHOLD_KB = 1024                 # KB
    THRESHOLD_MB = 1024 * 1024          # MB
    THRESHOLD_GB = 1024 * 1024 * 1024   # GB
    """
    stats = {
        'cpu_freq_percpu': psutil.cpu_freq(percpu=True),
        'cpu_freq': psutil.cpu_freq(percpu=False),
        'cpu_stats': psutil.cpu_stats(),
        'cpu_load_avg': psutil.getloadavg(),
        'cpu_count_logical': psutil.cpu_count(),
        'cpu_count_physical': psutil.cpu_count(logical=False),
        'cpu_times_percent': psutil.cpu_times_percent(1, False),
        'cpu_times_percent_percpu': psutil.cpu_times_percent(1, True),
        'cpu_percent': psutil.cpu_percent(interval=None),
        'cpu_percent_percpu': psutil.cpu_percent(interval=None, percpu=True),
        'memory': {
            'total_bytes': memory.total,
            'total_kb': memory.total / THRESHOLD_KB,
            'total_mb': memory.total / THRESHOLD_MB,
            'total_gb': memory.total / THRESHOLD_GB,

            'available_bytes': memory.available,
            'available_kb': memory.available / THRESHOLD_KB,
            'available_mb': memory.available / THRESHOLD_MB,
            'available_gb': memory.available / THRESHOLD_GB,

            'percentage': memory.percent,
    
            'used_bytes': memory.used,
            'used_kb': memory.used / THRESHOLD_KB,
            'used_mb': memory.used / THRESHOLD_MB,
            'used_gb': memory.used / THRESHOLD_GB,
        }
    }
    """
    stats = {
        'cpu': psutil.cpu_percent(interval=None),
        'ram': memory.percent,
        'docs': db.todo.count()
    }

    return jsonify(
        status=True,
        stats=stats
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
            'time': todo['time']
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
    current_time = now.strftime("%H:%M:%S")

    item = {
        'author': data['author'],
        'sentence': data['sentence'],
        'time': current_time
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
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)