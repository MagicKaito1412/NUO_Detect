from flask import Flask
import sys

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

scaler = StandardScaler()
model_logreg = LogisticRegression(solver='liblinear', C=0.003)
model_forest = RandomForestClassifier(n_estimators=25, max_depth=3, criterion='entropy',
                                      random_state=42, bootstrap=False)
model_svm = SVC(C=0.01, probability=True, kernel='linear', random_state=42)


app = Flask(__name__,)
app.url_map.strict_slashes = False
app.config['MODELS_PATH'] = sys.path[-1] + '/backend' + '/models'

import backend.model_training.controller
