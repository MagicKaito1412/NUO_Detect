from backend.form_report import app, service
from flask import request, current_app, send_from_directory
import os


@app.route('/doc_report', methods=['POST'])
def doc_report():
    data = request.get_json()
    filename = service.doc_report(data)
    return filename


@app.route('/patient_report', methods=['POST'])
def patient_report():
    data = request.get_json()
    filename = service.patient_report(data)
    return filename


@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)


@app.route('/remove/<path:filename>', methods=['GET'])
def remove(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    full_path = f"{uploads}{filename}"
    if os.path.exists(full_path):
        os.remove(full_path)
        return 'OK', 200
    return 'ALREADY DELETED', 410
