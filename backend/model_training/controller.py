from backend.model_training import app, service
from flask import request, jsonify
import requests


@app.route('/train', methods=['GET'])
def train():
    service.train()
    return 'OK', 200


@app.route('/calc_sens_spec', methods=['GET'])
def calc_sens_spec():
    result = service.calc_sens_spec()
    return jsonify(result), 200
