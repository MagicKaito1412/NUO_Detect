from backend.model_training import app, service
from flask import jsonify


@app.route('/train', methods=['POST'])
def train():
    service.train()
    return 'OK', 200


@app.route('/calc_sens_spec', methods=['GET'])
def calc_sens_spec():
    result = service.calc_sens_spec()
    return jsonify(result), 200


@app.route('/get_sens_spec', methods=['GET'])
def get_sens_spec():
    result = service.get_sens_spec()
    if result:
        return jsonify(result), 200
    else:
        return 'NOT OK', 200
