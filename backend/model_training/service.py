import pandas as pd
import sys
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from backend.model_training.core import get_train_val, get_X_y, get_sens_spec, get_train_ekg
from backend.utils.colnames import DB_EKG_USELESS_COLS


scaler = StandardScaler()
model_logreg = LogisticRegression(solver='liblinear', C=0.003)
model_forest = RandomForestClassifier(n_estimators=25, max_depth=3, criterion='entropy',
                                      random_state=42, bootstrap=False)
model_svm = SVC(C=0.01, probability=True, kernel='linear', random_state=42)


def train():
    data = get_train_ekg()
    X, y = get_X_y(data, useless_cols=DB_EKG_USELESS_COLS)
    X_scaled = scaler.fit_transform(X)
    model_logreg.fit(X_scaled, y)
    model_forest.fit(X_scaled, y)
    model_svm.fit(X_scaled, y)


def calc_sens_spec():
    data = get_train_ekg()
    metrics = get_sens_spec(data)
    return metrics
