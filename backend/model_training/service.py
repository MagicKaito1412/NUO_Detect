import pandas as pd
import sys
import numpy as np
import pickle as pkl

from backend.model_training.core import (
    get_train_val, get_X_y, get_sens_spec, get_train_ekg, save_models
)
from backend.utils.colnames import DB_EKG_USELESS_COLS

from backend.model_training import (
    scaler, model_logreg, model_forest, model_svm, app
)


def train():
    data = get_train_ekg()
    X, y = get_X_y(data, useless_cols=DB_EKG_USELESS_COLS)
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    model_logreg.fit(X_scaled, y)
    model_forest.fit(X_scaled, y)
    model_svm.fit(X_scaled, y)
    save_models()

    with open(f"{app.config['MODELS_PATH']}/svm.pkl", 'wb') as f:
        pkl.dump(model_svm, f)
    with open(f"{app.config['MODELS_PATH']}/forest.pkl", 'wb') as f:
        pkl.dump(model_forest, f)
    with open(f"{app.config['MODELS_PATH']}/logreg.pkl", 'wb') as f:
        pkl.dump(model_logreg, f)
    with open(f"{app.config['MODELS_PATH']}/scaler.pkl", 'wb') as f:
        pkl.dump(scaler, f)


def calc_sens_spec():
    data = get_train_ekg()
    metrics = get_sens_spec(data)
    return metrics
