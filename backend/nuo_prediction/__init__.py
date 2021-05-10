from flask import Flask
import sys
import pickle as pkl
from flask_cors import CORS

app = Flask(__name__,)
CORS(app)

app.url_map.strict_slashes = False
app.config['MODELS_PATH'] = sys.path[-1] + '/backend' + '/models'

try:
    with open(f"{app.config['MODELS_PATH']}/logreg.pkl", 'rb') as f:
        model_logreg = pkl.load(f)
except FileNotFoundError:
    model_logreg = False

try:
    with open(f"{app.config['MODELS_PATH']}/svm.pkl", 'rb') as f:
        model_svm = pkl.load(f)
except FileNotFoundError:
    model_svm = False

try:
    with open(f"{app.config['MODELS_PATH']}/forest.pkl", 'rb') as f:
        model_forest = pkl.load(f)
except FileNotFoundError:
    model_forest = False

try:
    with open(f"{app.config['MODELS_PATH']}/scaler.pkl", 'rb') as f:
        scaler = pkl.load(f)
except FileNotFoundError:
    scaler = False

import backend.nuo_prediction.controller
