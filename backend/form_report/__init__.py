from flask import Flask
from flask_cors import CORS

app = Flask(__name__,)
CORS(app)
app.url_map.strict_slashes = False
app.config['UPLOAD_FOLDER'] = "templates/"

import backend.form_report.controller
