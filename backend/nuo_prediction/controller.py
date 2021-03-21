from . import service
from run import app


@app.route('/predict/<int:patient_id>', methods=['POST'])
def predict(patient_id):
    service.predict(patient_id)

