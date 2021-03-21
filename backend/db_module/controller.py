from backend.db_module import app, service
from flask import request


@app.route('/export_csv', methods=['POST'])
def export_csv():
    filename = request.form.get('filename')
    service.export_csv(filename)
    return 'OK', 200


@app.route('/get_patient', methods=['GET'])
def get_patient_ekg():
    polis_id = request.form.get('polis_id')
    pass


@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = dict(
        first_name=request.form.get('first_name'),
        last_name=request.form.get('last_name'),
        middle_name=request.form.get('middle_name'),
        gender=request.form.get('gender'),
        age=request.form.get('age'),
        weight=request.form.get('weight'),
        height=request.form.get('height'),
        has_nuo=request.form.get('has_nuo'),
        policy_num=request.form.get('policy_num'),
        prob_log_reg="-1",
        prob_rnd_forest="-1",
        prob_log_svm="-1"
    )
    pass


@app.route('/insert_update_ekg', methods=['POST'])
def insert_ekg():
    data = dict(
        first_name=request.form.get('first_name'),
        last_name=request.form.get('last_name'),
        middle_name=request.form.get('middle_name'),
        gender=request.form.get('gender'),
        age=request.form.get('age'),
        weight=request.form.get('weight'),
        height=request.form.get('height'),
        has_nuo=request.form.get('has_nuo'),
        policy_num=request.form.get('policy_num'),
        prob_log_reg="-1",
        prob_rnd_forest="-1",
        prob_log_svm="-1"
    )


@app.route('/info', methods=['GET'])
def info():
    return 'OK', 200
