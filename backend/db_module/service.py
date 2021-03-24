import pandas as pd
import os
import random
import sys
import psycopg2
from dateutil.relativedelta import relativedelta
from datetime import datetime

from backend.db_module import app
from backend.utils.colnames import (
    ID, FIO, TYPE, AGE, WEIGHT, HEIGHT, PROB_LOG_REG, PROB_RND_FOREST, PROB_SVM,
    ECG, DATE, NOISY_COLS, USELESS_COLS, DISRESPECT_COLS, TARGET_COL, DB_REGISTRY_DATE,
    COLUMN_MAP, DB_PROB_LOG_REG, DB_PROB_RND_FOREST, DB_PROB_SVM, EKG_COLUMNS
)
from backend.utils.connect import db_transaction


@db_transaction
def export_csv(conn, cur, filename):
    def reldate(x):
        return relativedelta(x['Дата/Время съема ЭКГ/глюкозы'], x['Дата рождения']).years

    data = pd.read_csv(filename)
    data['Дата рождения'] = pd.to_datetime(data['Дата рождения'])
    data['Дата/Время съема ЭКГ/глюкозы'] = pd.to_datetime(
        data['Дата/Время съема ЭКГ/глюкозы'])
    if AGE not in data.columns:
        data[AGE] = data.apply(reldate, axis=1)
    data[PROB_LOG_REG] = -1
    data[PROB_RND_FOREST] = -1
    data[PROB_SVM] = -1
    data[TARGET_COL] = data[TARGET_COL].astype(int)

    added_patients = set()
    last_nuo = -1
    last_patient_id = -1

    for i, row in data.iterrows():
        if row[ID] not in added_patients:
            added_patients.add(row[ID])
            cur.execute("SELECT nextval(pg_get_serial_sequence('users', 'user_id'))")
            user_id = cur.fetchone()[0]

            user_data = dict(
                user_id=user_id,
                login=f'user{user_id}',
                password=f'user{user_id}',
                access_level=0
            )
            cur.execute(f"INSERT INTO users({', '.join(user_data.keys())}) "
                        f"VALUES ({','.join(['%s'] * len(user_data))})",
                        (tuple(user_data.values()))
                        )

            cur.execute("SELECT nextval(pg_get_serial_sequence('patients', 'patient_id'))")
            patient_id = cur.fetchone()[0]
            patient_data = {
                'patient_id': patient_id,
                'user_id': user_id,
                'policy_num': ''.join([str(random.randint(0, 9)) for _ in range(16)]),
                'first_name': f'user{len(added_patients)}',
                'last_name': f'user{len(added_patients)}',
                'middle_name': f'user{len(added_patients)}',
                'gender': row[TYPE],
                'age': row[AGE],
                'weight': row[WEIGHT],
                'height': row[HEIGHT],
                'has_nuo': -1,
                'prob_log_reg': -1,
                'prob_rnd_forest': -1,
                'prob_log_svm': -1
            }
            cur.execute(f"INSERT INTO patients({', '.join(patient_data.keys())}) "
                        f"VALUES ({','.join(['%s'] * len(patient_data))})",
                        (tuple(patient_data.values()))
                        )
            conn.commit()

            if len(added_patients) > 1:
                cur.execute(f"UPDATE patients SET has_nuo = {last_nuo} WHERE patient_id = {last_patient_id}")
                conn.commit()

        nuo = row[TARGET_COL]
        if nuo != -1 and nuo != 1:
            nuo = 0
        last_nuo = nuo
        last_patient_id = patient_id

        ekg_data = dict(zip(COLUMN_MAP.keys(), row[COLUMN_MAP.keys()]))
        ekg_data['registry_date'] = row['Дата/Время съема ЭКГ/глюкозы']
        ekg_data['patient_id'] = patient_id
        ekg_data['prob_log_reg'] = -1
        ekg_data['prob_rnd_forest'] = -1
        ekg_data['prob_log_svm'] = -1
        ekg_data['has_nuo'] = nuo
        ekg_data.pop('номер ЭКГ')
        ekg_data.pop('Дата/Время съема ЭКГ/глюкозы')
        query = (
            (f"INSERT INTO ekgs({', '.join(ekg_data.keys())}) "
             f"VALUES ({','.join(['%s'] * len(ekg_data))})")
        )
        cur.execute(query, tuple(ekg_data.values()))
        conn.commit()


@db_transaction
def update_ekg(conn, cur, data):
    ekg_id = data.pop('ekg_id')
    subquery = ', '.join([f'{k}=%s' for k in data.keys()])
    cur.execute(
        f"UPDATE ekgs SET {subquery} WHERE ekg_id=%s",
        (tuple(data.values()) + (ekg_id,))
    )
    conn.commit()


@db_transaction
def insert_ekg(conn, cur, data):
    cur.execute("SELECT nextval(pg_get_serial_sequence('ekgs', 'ekg_id'))")
    ekg_id = cur.fetchone()[0]
    data['ekg_id'] = ekg_id
    cur.execute(
        f"INSERT INTO ekgs({', '.join(data.keys())})"
        f"VALUES ({','.join(['%s'] * len(data))})",
        (tuple(data.values()))
    )
    conn.commit()


# NEED TEST
@db_transaction
def update_patient(conn, cur, patient_data):
    patient_id = patient_data.pop('patient_id')
    subquery = ', '.join([f'{k}=%s' for k in patient_data.keys()])
    cur.execute(
        f"UPDATE patients SET {subquery} WHERE patient_id=%s",
        (tuple(patient_data.values()) + (patient_id,))
    )
    conn.commit()


@db_transaction
def insert_patient(conn, cur, patient_data):
    cur.execute("SELECT nextval(pg_get_serial_sequence('users', 'user_id'))")
    user_id = cur.fetchone()[0]

    user_data = dict(
        user_id=user_id,
        login=f'user{user_id}',
        password=f'user{user_id}',
        access_level=0
    )
    cur.execute(
        f"INSERT INTO users({', '.join(user_data.keys())}) "
        f"VALUES ({','.join(['%s'] * len(user_data))})",
        (tuple(user_data.values()))
    )

    cur.execute("SELECT nextval(pg_get_serial_sequence('patients', 'patient_id'))")
    patient_id = cur.fetchone()[0]

    patient_data['patient_id'] = patient_id
    patient_data['user_id'] = user_id
    cur.execute(
        f"INSERT INTO patients({', '.join(patient_data.keys())}) "
        f"VALUES ({','.join(['%s'] * len(patient_data))})",
        (tuple(patient_data.values()))
    )
    conn.commit()


@db_transaction
def get_all_patients(conn, cur):
    cols = (
        'patient_id', 'first_name', 'last_name', 'middle_name', 'gender', 'age', 'policy_num',
    )
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT {','.join(cols)} "
        "FROM patients"
        ") data"
    )
    data = []
    for d in cur:
        data.append(d[0])
    return data


@db_transaction
def get_patients(conn, cur, filters):
    cols = (
        'patient_id', 'first_name', 'last_name', 'middle_name', 'gender', 'age', 'policy_num',
    )

    subquery_in = [f"POSITION('{value.lower()}' IN LOWER(patients.{col})) = 1" for col, value in filters.items()]
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT {','.join(cols)} "
        "FROM patients "
        f"WHERE {' AND '.join(subquery_in)}"
        ") data"
    )
    data = []
    for d in cur:
        data.append(d[0])
    return data


@db_transaction
def get_patient_ekgs(conn, cur, policy_num):
    exec_cols = (
        'ekg_id', 'registry_date'
    )
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT {','.join(exec_cols)} "
        "FROM ekgs LEFT JOIN patients ON ekgs.patient_id = patients.patient_id "
        f"WHERE patients.policy_num = '{policy_num}'"
        ") data"
    )
    data = []
    for d in cur:
        data.append(d[0])
    return data


@db_transaction
def get_ekg(conn, cur, ekg_id):
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT {','.join(EKG_COLUMNS)} "
        "FROM ekgs "
        f"WHERE ekgs.ekg_id = {ekg_id}"
        ") data"
    )
    data = cur.fetchone()[0]
    return data


@db_transaction
def delete_patient(conn, cur, patient_id):
    cur.execute(f"SELECT user_id FROM patients WHERE patient_id = {patient_id}")
    user_id = cur.fetchone()[0]
    cur.execute(f"DELETE FROM users WHERE user_id = {user_id}")
    conn.commit()


@db_transaction
def delete_ekg(conn, cur, ekg_id):
    cur.execute(f"DELETE FROM ekgs WHERE ekg_id = {ekg_id}")
    conn.commit()
