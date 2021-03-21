import pandas as pd
import random
import psycopg2
from dateutil.relativedelta import relativedelta
from backend.db_module import app
from backend.db_module.utils.colnames import (
    ID, FIO, TYPE, AGE, WEIGHT, HEIGHT, PROB_LOG_REG, PROB_RND_FOREST, PROB_SVM,
    ECG, DATE, BAD_COLS, NOISY_COLS, USELESS_COLS, DISRESPECT_COLS, TARGET_COL,
    COLUMN_MAP
)


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
    data[TARGET_COL] = (data[TARGET_COL] == 1).astype(int)

    conn = psycopg2.connect(dbname='nuo_detect',
                            user='u1',
                            password='1',
                            host='127.0.0.1')
    cur = conn.cursor()
    added_patients = set()

    for i, row in data.iterrows():
        if row[ID] not in added_patients:
            added_patients.add(row[ID])
            cur.execute("select nextval(pg_get_serial_sequence('users', 'user_id'))")
            user_id = cur.fetchone()[0]

            user_data = dict(
                login=f'user{len(added_patients)}',
                password=f'user{len(added_patients)}',
                access_level=0
            )
            cur.execute(f"insert into users(user_id, {', '.join(user_data.keys())}) "
                        f"values ({','.join(['%s'] * (len(user_data)+1))})",
                        ((user_id, ) + tuple(user_data.values()))
                        )
            conn.commit()

            cur.execute("select nextval(pg_get_serial_sequence('patients', 'patient_id'))")
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
                'has_nuo': False,
                'prob_log_reg': -1,
                'prob_rnd_forest': -1,
                'prob_log_svm': -1
            }
            cur.execute(f"insert into patients(patient_id, {', '.join(patient_data.keys())}) "
                        f"values ({','.join(['%s'] * (len(patient_data)+1))})",
                        ((patient_id, ) + tuple(patient_data.values()))
                        )
            conn.commit()

        row = dict(zip(COLUMN_MAP.keys(), row[COLUMN_MAP.keys()]))
        row['registry_date'] = row['Дата/Время съема ЭКГ/глюкозы']
        row['patient_id'] = patient_id
        row.pop('номер ЭКГ')
        row.pop('Дата/Время съема ЭКГ/глюкозы')
        query = (
            (f"insert into ekgs({', '.join(row.keys())}) "
             f"values ({','.join(['%s'] * len(row))})")
        )
        cur.execute(query, tuple(row.values()))
    conn.commit()
    return '', 200


def get_all_ekg_csv():
    conn = psycopg2.connect(dbname='nuo_detect',
                            user='u1',
                            password='1',
                            host='127.0.0.1')
    cur = conn.cursor()
    cur.execute("select * from ekgs")
