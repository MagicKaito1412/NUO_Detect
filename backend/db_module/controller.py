from backend.db_module import app, service
from flask import request, jsonify


@app.route('/info', methods=['GET'])
def info():
    return 'OK', 200


@app.route('/export_csv', methods=['POST'])
def export_csv():
    filename = request.form.get('filename')
    service.export_csv(filename)
    return 'OK', 200


@app.route('/update_patient', methods=['POST'])
def update_patient():
    data = request.get_json()
    if data.get('patient_id'):
        service.update_patient(data)
        return 'OK', 200
    return 'check patient_id', 400


patient_not_null_cols = set(['first_name', 'last_name', 'gender', 'age', 'weight', 'height', 'policy_num'])
@app.route('/insert_patient', methods=['POST'])
def insert_patient():
    data = request.get_json()
    diff = patient_not_null_cols - (patient_not_null_cols & data.keys())
    if not diff:
        service.insert_patient(data)
        return 'OK', 200
    s = str(tuple(diff.values()))
    return f"check {s}", 400


@app.route('/update_ekg/', methods=['POST'])
def update_ekg():
    data = request.get_json()
    if data.get('ekg_id'):
        service.update_ekg(data)
        return 'OK', 200
    return 'check ekg_id', 400


ekg_not_null_cols = set(['first_name', 'last_name', 'gender', 'age', 'weight', 'height', 'policy_num'])
@app.route('/inset_ekg', methods=['POST'])
def inset_ekg():
    data = request.get_json()
    diff = ekg_not_null_cols - (ekg_not_null_cols & data.keys())
    if not diff:
        service.inset_ekg(data)
        return 'OK', 200
    return 'check ekg_id, patient_id, registry_date', 400


@app.route('/get_patients', methods=['GET'])
def get_patients():
    result = service.get_patients()
    return jsonify(result)


@app.route('/get_patient_ekgs/<string:policy_num>', methods=['GET'])
def get_patient_ekgs(policy_num):
    result = service.get_patient_ekgs(policy_num)
    return jsonify(result)


@app.route('/get_ekg/<int:ekg_id>', methods=['GET'])
def get_ekg(ekg_id):
    result = service.get_ekg(ekg_id)
    return jsonify(result)
