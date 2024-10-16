from flask import Flask, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/api/data')
def get_data():
    with open('/etc/hostname', 'r') as f:
        container_name = f.read().strip()
    data = {
        "container_name": container_name,
        "response": "Response from "+container_name
    }
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)