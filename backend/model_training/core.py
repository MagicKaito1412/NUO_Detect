import numpy as np
import pandas as pd
import psycopg2
from sklearn.metrics import f1_score, recall_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from backend.utils.colnames import (
    DB_PROB_LOG_REG, DB_PROB_RND_FOREST, DB_PROB_SVM,
    NOISY_COLS, DB_TARGET_COL, EKG_COLUMNS,
    DB_EKG_USELESS_COLS, DB_PATIENT_ID
)

def get_train_ekg():
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
                "WHERE ekgs.has_nuo != -1")

    data = cur.fetchall()
    df = pd.DataFrame(data=data, columns=df_cols)
    return df


def get_train_val(X, y, useless_cols=None, test_size=0.3, random_state=42, patients=None, k_choice=None):
    patients_num = X[DB_PATIENT_ID].unique()

    if patients is None:
        train_patients = np.random.choice(patients_num, int(
            len(patients_num) * (1 - test_size)), replace=False)
        test_patients = set(patients_num) - set(train_patients)
    else:
        try:
            assert k_choice is not None
        except AssertionError as e:
            e.args += ('k_choice cannot be None',)
            raise

        if k_choice + k_choice // 5 > len(patients):
            k_choice = len(patients)
        test_patients = np.random.choice(patients, k_choice, replace=False)
        train_patients = set(patients_num) - set(test_patients)

    train_ids = X[DB_PATIENT_ID].apply(
        lambda x: x in train_patients)
    X_train = X[train_ids]
    y_train = y[train_ids]

    val_ids = X[DB_PATIENT_ID].apply(lambda x: x in test_patients)
    X_val = X[val_ids]
    y_val = y[val_ids]

    if useless_cols:
        X_train = X_train.drop(labels=useless_cols, axis=1)
        X_val = X_val.drop(labels=useless_cols, axis=1)

    if len(patients):
        return X_train, X_val, y_train, y_val, test_patients
    return X_train, X_val, y_train, y_val

def get_X_y(data, useless_cols=None):
    X = data.copy()
    X = X.drop(labels=NOISY_COLS, axis=1)
    if useless_cols:
        X = X.drop(labels=useless_cols, axis=1)

    drop_inds = X[set(X.columns) - set(DB_EKG_USELESS_COLS)].isna().sum(axis=1)
    drop_inds = drop_inds[drop_inds > 0]
    X = X.drop(labels=drop_inds.index)

    y = X[DB_TARGET_COL]
    y = (y == 1).astype(int).values.flatten()
    X = X.drop(labels=[DB_TARGET_COL], axis=1)

    return X, y


def get_sens_spec(data, save_predicts=False):
    X, y = get_X_y(data)

    patients_num = X[DB_PATIENT_ID].unique()

    k = int(len(patients_num) * (3 / 7))
    f1_lst_logreg = []
    recall_true_logreg = []
    recall_false_logreg = []

    f1_lst_forest = []
    recall_true_forest = []
    recall_false_forest = []

    f1_lst_svm = []
    recall_true_svm = []
    recall_false_svm = []

    iteration = 0
    while len(patients_num):
        np.random.seed(42)
        model_logreg = LogisticRegression(solver='liblinear', C=0.003)
        model_forest = RandomForestClassifier(n_estimators=25, max_depth=3, criterion='entropy',
                                              random_state=42, bootstrap=False)
        model_svm = SVC(C=0.01, probability=True, kernel='linear', random_state=42)

        X_train, X_val, y_train, y_val, ids = get_train_val(X, y, useless_cols=DB_EKG_USELESS_COLS,
                                                            patients=patients_num, k_choice=k)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_val_scaled = scaler.transform(X_val)
        model_logreg.fit(X_train_scaled, y_train)
        model_forest.fit(X_train_scaled, y_train)
        model_svm.fit(X_train_scaled, y_train)

        pred_logreg_proba = model_logreg.predict_proba(X_val_scaled)
        pred_logreg = np.round(pred_logreg_proba[:, 1]).astype(int)
        f1_lst_logreg.append(f1_score(y_val, pred_logreg))
        recall_true_logreg.append(recall_score(y_val, pred_logreg))
        recall_false_logreg.append(recall_score((~y_val.astype(bool)).astype(
            int), (~pred_logreg.astype(bool)).astype(int)))
        data.loc[X_val.index, DB_PROB_LOG_REG] = np.round(pred_logreg_proba[:, 1], 2)

        pred_forest_proba = model_forest.predict_proba(X_val_scaled)
        pred_forest = np.round(pred_forest_proba[:, 1]).astype(int)
        f1_lst_forest.append(f1_score(y_val, pred_forest))
        recall_true_forest.append(recall_score(y_val, pred_forest))
        recall_false_forest.append(recall_score((~y_val.astype(bool)).astype(
            int), (~pred_forest.astype(bool)).astype(int)))
        data.loc[X_val.index, DB_PROB_RND_FOREST] = np.round(pred_forest_proba[:, 1], 2)

        pred_svm_proba = model_svm.predict_proba(X_val_scaled)
        pred_svm = np.round(pred_svm_proba[:, 1]).astype(int)
        f1_lst_svm.append(f1_score(y_val, pred_svm))
        recall_true_svm.append(recall_score(y_val, pred_svm))
        recall_false_svm.append(recall_score((~y_val.astype(bool)).astype(
            int), (~pred_svm.astype(bool)).astype(int)))
        data.loc[X_val.index, DB_PROB_SVM] = np.round(pred_svm_proba[:, 1], 2)

        patients_num = list(set(patients_num) - set(ids))
        iteration += 1

    f1_lst_logreg = np.array(f1_lst_logreg)
    sensitivity_logreg = np.array(recall_true_logreg)
    specificity_logreg = np.array(recall_false_logreg)

    f1_lst_forest = np.array(f1_lst_forest)
    sensitivity_forest = np.array(recall_true_forest)
    specificity_forest = np.array(recall_false_forest)

    f1_lst_svm = np.array(f1_lst_svm)
    sensitivity_svm = np.array(recall_true_svm)
    specificity_svm = np.array(recall_false_svm)

    models_metrics = dict(
        logreg_f1=f1_lst_logreg.mean(),
        logreg_sensitivity=sensitivity_logreg.mean(),
        logreg_specificity=specificity_logreg.mean(),
        forest_f1=f1_lst_forest.mean(),
        forest_sensitivity=sensitivity_forest.mean(),
        forest_specificity=specificity_forest.mean(),
        svm_f1=f1_lst_svm.mean(),
        svm_sensitivity=sensitivity_svm.mean(),
        svm_specificity=specificity_svm.mean()
    )

    if save_predicts:
        return models_metrics, data
    return models_metrics
