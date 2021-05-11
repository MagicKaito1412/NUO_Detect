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
    full_file_path = f"{uploads}{filename}"
    full_svg_path = f"{uploads}img.svg"
    full_img_path = f"{uploads}img.jpg"
    if os.path.exists(full_file_path):
        os.remove(full_file_path)
    if os.path.exists(full_svg_path):
        os.remove(full_svg_path)
    if os.path.exists(full_img_path):
        os.remove(full_img_path)
    return 'OK', 200
