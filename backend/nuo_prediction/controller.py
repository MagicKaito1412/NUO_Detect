from backend.nuo_prediction import app, service


@app.route('/predict/<int:patient_id>', methods=['POST'])
def predict(patient_id):
    service.predict(patient_id)
    return 'OK', 200
