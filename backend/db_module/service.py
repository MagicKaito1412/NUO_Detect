import pandas as pd
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
        # print(row.index)
        if row[ID] not in added_patients:
            added_patients.add(row[ID])
            cur.execute("insert into public.users(login, password, access_level) "
                        "values (%s, %s, %s)",
                        (f'user{len(added_patients)}', f'user{len(added_patients)}', 0)
                        )
            conn.commit()

            patient_data = {
                'user_id': len(added_patients),
                'first_name': f'user{len(added_patients)}',
                'last_name': f'user{len(added_patients)}',
                'middle_name': f'user{len(added_patients)}',
                TYPE: row[TYPE],
                AGE: row[AGE],
                WEIGHT: row[WEIGHT],
                HEIGHT: row[HEIGHT],
                'has_nuo': False,
                PROB_LOG_REG: -1,
                PROB_RND_FOREST: -1,
                PROB_SVM: -1
            }

            cur.execute("insert into public.patients(user_id, first_name, last_name, middle_name, gender, age, weight,"
                        "height, has_nuo, prob_log_reg, prob_rnd_forest, prob_log_svm) "
                        "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (tuple(patient_data.values()))
                        )
            conn.commit()

        row = dict(zip(COLUMN_MAP.keys(), row[COLUMN_MAP.keys()]))
        row['registry_date'] = row['Дата/Время съема ЭКГ/глюкозы']
        row['patient_id'] = len(added_patients)
        row.pop('номер ЭКГ')
        row.pop('Дата/Время съема ЭКГ/глюкозы')
        query = (
            (f"insert into ekgs({', '.join(row.keys())}) "
             f"values ({','.join(['%s'] * len(row))})")
        )
        cur.execute(query, tuple(row.values()))
    conn.commit()
    return '', 200
