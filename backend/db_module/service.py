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
    COLUMN_MAP, DB_PROB_LOG_REG, DB_PROB_RND_FOREST, DB_PROB_SVM
)

conn = psycopg2.connect(dbname='nuo_detect',
                        user='u1',
                        password='1',
                        host='127.0.0.1')
cur = conn.cursor()


def export_csv(filename):
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
                login=f'user{user_id}',
                password=f'user{user_id}',
                access_level=0
            )
            cur.execute(f"INSERT INTO users(user_id, {', '.join(user_data.keys())}) "
                        f"VALUES ({','.join(['%s'] * (len(user_data)+1))})",
                        ((user_id, ) + tuple(user_data.values()))
                        )
            conn.commit()

            cur.execute("SELECT nextval(pg_get_serial_sequence('patients', 'patient_id'))")
            patient_id = cur.fetchone()[0]
            patient_data = {
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
            cur.execute(f"INSERT INTO patients(patient_id, {', '.join(patient_data.keys())}) "
                        f"VALUES ({','.join(['%s'] * (len(patient_data)+1))})",
                        ((patient_id, ) + tuple(patient_data.values()))
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


def update_ekg(data):
    DB_PROB_LOG_REG, DB_PROB_RND_FOREST, DB_PROB_SVM
    cur.execute(f"UPDATE ekgs SET "
                f"{DB_PROB_LOG_REG}=%s, "
                f"{DB_PROB_RND_FOREST}=%s, "
                f"{DB_PROB_SVM}=%s "
                f"WHERE ekg_id = %s",
                (data[DB_PROB_LOG_REG], data[DB_PROB_RND_FOREST], data[DB_PROB_SVM], data['ekg_id']))
    conn.commit()
