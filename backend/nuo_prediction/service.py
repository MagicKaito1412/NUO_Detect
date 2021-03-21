from flask import jsonify

import psycopg2
import pandas as pd
import requests


from backend.utils.colnames import (
    DB_PROB_LOG_REG, DB_PROB_RND_FOREST, DB_PROB_SVM,
    NOISY_COLS, DB_TARGET_COL, EKG_COLUMNS,
    DB_EKG_USELESS_COLS, DB_PATIENT_ID, DB_REGISTRY_DATE
)
from backend.model_training.core import get_X_y
from backend.nuo_prediction import (
    scaler, model_forest, model_logreg, model_svm
)


def get_predict_patient_ekg(patient_id):
    df_cols = ('gender', 'age', 'weight', 'height') + tuple(EKG_COLUMNS)

    conn = psycopg2.connect(dbname='nuo_detect',
                            user='u1',
                            password='1',
                            host='127.0.0.1')
    cur = conn.cursor()

    exec_cols = ('patients.gender', 'patients.age', 'patients.weight', 'patients.height') + \
        tuple(map(lambda x: 'ekgs.' + x, EKG_COLUMNS))
    cur.execute(f"SELECT {','.join(exec_cols)} "
                "FROM ekgs LEFT JOIN patients ON ekgs.patient_id = patients.patient_id "
                f"WHERE ekgs.has_nuo = -1 AND patients.patient_id = {patient_id}")

    data = cur.fetchall()
    df = pd.DataFrame(data=data, columns=df_cols)
    return df


def predict(patient_id):
    data = get_predict_patient_ekg(patient_id)
    X, y = get_X_y(data, useless_cols=DB_EKG_USELESS_COLS)

    X_scaled = scaler.transform(X)
    pred_logreg_proba = model_logreg.predict_proba(X_scaled)[:, 1]
    pred_forest_proba = model_forest.predict_proba(X_scaled)[:, 1]
    pred_svm_proba = model_svm.predict_proba(X_scaled)[:, 1]

    for i, val in data.iterrows():
        json_data = {
            DB_PROB_LOG_REG: pred_logreg_proba[i],
            DB_PROB_RND_FOREST: pred_forest_proba[i],
            DB_PROB_SVM: pred_svm_proba[i],
            'ekg_id': val['ekg_id'],
        }
        requests.post(url='http://127.0.0.1:5000/update_ekg', json=json_data)
