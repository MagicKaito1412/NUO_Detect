from backend.db_module import service
from flask import request
from backend.db_module import app


@app.route('/export_csv', methods=['POST'])
def export_csv():
    filename = request.form.get('filename')
    service.export_csv(filename)
    return 'OK', 200


@app.route('/info', methods=['GET'])
def hello():
    return 'hello', 200
