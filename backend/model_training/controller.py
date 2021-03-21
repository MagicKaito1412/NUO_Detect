from backend.model_training import app, service
from flask import request, jsonify
import requests


@app.route('/train', methods=['GET'])
def train():
    response = requests.request(method='GET',
                                url='http://127.0.0.1:5001/info')
    print(response)
    service.train()
    return 'OK', 200
