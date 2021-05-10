from backend.nuo_prediction import app, service


@app.route('/predict/<int:patient_id>', methods=['POST'])
def predict(patient_id):
    result = service.predict(patient_id)
    if result:
        return 'OK', 200
    else:
        return 'NOT OK', 200
