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
        user_id, patient_id = service.insert_patient(data)
        data['user_id'] = user_id
        data['patient_id'] = patient_id
        return jsonify(data), 200
    s = str(tuple(diff.values()))
    return f"check {s}", 400


@app.route('/update_ekg/', methods=['POST'])
def update_ekg():
    data = request.get_json()
    if data.get('ekg_id'):
        service.update_ekg(data)
        return 'OK', 200
    return 'check ekg_id', 400


ekg_not_null_cols = set(['registry_date'])
@app.route('/insert_ekg', methods=['POST'])
def insert_ekg():
    data = request.get_json()
    diff = ekg_not_null_cols - (ekg_not_null_cols & data.keys())
    if not diff:
        service.insert_ekg(data)
        return 'OK', 200
    return 'check registry_date', 400


@app.route('/get_all_patients', methods=['GET'])
def get_all_patients():
    result = service.get_all_patients()
    return jsonify(result)


@app.route('/get_patients', methods=['POST'])
def get_patients():
    filters = request.get_json()
    result = service.get_patients(filters)
    return jsonify(result)


@app.route('/get_patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    result = service.get_patient(patient_id)
    return jsonify(result)


@app.route('/get_patient_ekgs/<string:patient_id>', methods=['GET'])
def get_patient_ekgs(patient_id):
    result = service.get_patient_ekgs(patient_id)
    return jsonify(result)


@app.route('/get_ekg/<int:ekg_id>', methods=['GET'])
def get_ekg(ekg_id):
    result = service.get_ekg(ekg_id)
    return jsonify(result)


@app.route('/delete_patient/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    service.delete_patient(patient_id)
    return 'OK', 200


@app.route('/delete_ekg/<int:ekg_id>', methods=['DELETE'])
def delete_ekg(ekg_id):
    service.delete_ekg(ekg_id)
    return 'OK', 200
