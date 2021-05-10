import pandas as pd
import os
from io import StringIO
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
def export_csv(conn, cur, file):
    def reldate(x):
        return relativedelta(x['Дата/Время съема ЭКГ/глюкозы'], x['Дата рождения']).years

    data = pd.read_csv(StringIO(file.read().decode('utf-8')))
    data['Дата рождения'] = pd.to_datetime(data['Дата рождения'])
    data['Дата/Время съема ЭКГ/глюкозы'] = pd.to_datetime(
        data['Дата/Время съема ЭКГ/глюкозы'])
    if AGE not in data.columns:
        data[AGE] = data.apply(reldate, axis=1)
    # data[PROB_LOG_REG] = -1
    # data[PROB_RND_FOREST] = -1
    # data[PROB_SVM] = -1
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
                access_level=3
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
                'first_name': f'first_user{len(added_patients)}',
                'last_name': f'last_user{len(added_patients)}',
                'middle_name': f'middle_user{len(added_patients)}',
                'gender': row[TYPE],
                'age': row[AGE],
                'weight': row[WEIGHT],
                'height': row[HEIGHT],
                'has_nuo': -1,
                # 'prob_log_reg': -1,
                # 'prob_rnd_forest': -1,
                # 'prob_log_svm': -1
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
        access_level=3
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
    return user_id, patient_id


@db_transaction
def insert_doctor(conn, cur, doctor_data):
    cur.execute("SELECT nextval(pg_get_serial_sequence('users', 'user_id'))")
    user_id = cur.fetchone()[0]

    user_data = dict(
        user_id=user_id,
        login=f'doctor{user_id}',
        password=f'doctor{user_id}',
        access_level=2
    )
    cur.execute(
        f"INSERT INTO users({', '.join(user_data.keys())}) "
        f"VALUES ({','.join(['%s'] * len(user_data))})",
        (tuple(user_data.values()))
    )

    cur.execute("SELECT nextval(pg_get_serial_sequence('doctors', 'doctor_id'))")
    doctor_id = cur.fetchone()[0]

    doctor_data['doctor_id'] = doctor_id
    doctor_data['user_id'] = user_id
    cur.execute(
        f"INSERT INTO doctors({', '.join(doctor_data.keys())}) "
        f"VALUES ({','.join(['%s'] * len(doctor_data))})",
        (tuple(doctor_data.values()))
    )
    conn.commit()
    return user_id, doctor_id


@db_transaction
def update_doctor(conn, cur, doctor_data):
    doctor_id = doctor_data.pop('doctor_id')
    subquery = ', '.join([f'{k}=%s' for k in doctor_data.keys()])
    cur.execute(
        f"UPDATE doctors SET {subquery} WHERE doctor_id=%s",
        (tuple(doctor_data.values()) + (doctor_id,))
    )
    conn.commit()


@db_transaction
def update_user(conn, cur, user_data):
    user_id = user_data.pop('user_id')
    subquery = ', '.join([f'{k}=%s' for k in user_data.keys()])
    cur.execute(
        f"UPDATE users SET {subquery} WHERE user_id=%s",
        (tuple(user_data.values()) + (user_id,))
    )
    conn.commit()


@db_transaction
def get_all_doctors(conn, cur):
    cols = (
        'doctor_id', 'first_name', 'last_name', 'middle_name', 'telephone',
    )
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT {','.join(cols)} "
        "FROM doctors"
        ") data"
    )
    data = []
    for d in cur:
        data.append(d[0])
    return data


@db_transaction
def get_doctors(conn, cur, filters):
    cols = (
        'doctor_id', 'first_name', 'last_name', 'middle_name', 'telephone',
    )
    if not filters:
        filters = dict(first_name="")
    subquery_in = [f"POSITION('{value.lower()}' IN LOWER(doctors.{col})) = 1" for col, value in filters.items()]
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT {','.join(cols)} "
        "FROM doctors "
        f"WHERE {' AND '.join(subquery_in)}"
        ") data"
    )
    data = []
    for d in cur:
        data.append(d[0])
    return data


@db_transaction
def get_patients_from_db(conn, cur):
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT * "
        "FROM patients"
        ") data"
    )
    data = []
    for d in cur:
        data.append(d[0])
    return data


@db_transaction
def get_all_patients(conn, cur):
    cols = (
        'patient_id', 'first_name', 'last_name', 'middle_name', 'age', 'policy_num',
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
def get_patient(conn, cur, patient_id):
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT * "
        "FROM patients "
        f"WHERE patients.patient_id = {patient_id} "
        ") data"
    )
    data = cur.fetchone()[0]
    return data


def get_stat():
    patients = get_patients_from_db()
    data = {}
    gender_count_values = {
        'men': 0,
        'women': 0
    }
    gender_ages_values = {
        'men': [0, 0, 0],
        'women': [0, 0, 0]
    }
    # todo add fucking bmi
    # bmi_values = {
    #     'value_16_18': 0,
    #     'value_19_25': 0,
    #     'value_26_30': 0,
    #     'value_31_35': 0,
    #     'value_36_40': 0,
    #     'value_41': 0
    # }
    nuo_values = {
        'has_nuo': 0,
        'has_not_nuo': 0
    }

    for patient in patients:
        if 18 <= patient.get('age') <= 44:
            if patient.get('gender') == 1:
                gender_count_values['men'] += 1
                gender_ages_values['men'][0] += 1
            if patient.get('gender') == 2:
                gender_count_values['women'] += 1
                gender_ages_values['women'][0] += 1
        if 45 <= patient.get('age') <= 64:
            if patient.get('gender') == 1:
                gender_count_values['men'] += 1
                gender_ages_values['men'][1] += 1
            if patient.get('gender') == 2:
                gender_count_values['women'] += 1
                gender_ages_values['women'][1] += 1
        if patient.get('age') >= 65:
            if patient.get('gender') == 1:
                gender_count_values['men'] += 1
                gender_ages_values['men'][2] += 1
            if patient.get('gender') == 2:
                gender_count_values['women'] += 1
                gender_ages_values['women'][2] += 1

        if patient.get('has_nuo') == 1:
            nuo_values['has_nuo'] += 1
        if patient.get('has_nuo') == 0:
            nuo_values['has_not_nuo'] += 1

    data['genderCountValues'] = gender_count_values
    data['genderAgesValues'] = gender_ages_values
    data['nuoValues'] = nuo_values
    return data


@db_transaction
def get_doctor(conn, cur, doctor_id):
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT * "
        "FROM doctors "
        f"WHERE doctors.doctor_id = {doctor_id} "
        ") data"
    )
    data = cur.fetchone()[0]
    return data


@db_transaction
def get_user_by_id(conn, cur, user_id):
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT * "
        "FROM users "
        f"WHERE users.user_id = {user_id} "
        ") data"
    )
    data = cur.fetchone()[0]
    return data


@db_transaction
def get_patients(conn, cur, filters):
    cols = (
        'patient_id', 'first_name', 'last_name', 'middle_name', 'gender', 'age', 'policy_num',
    )
    if not filters:
        filters = dict(first_name="")
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
def get_patient_ekgs(conn, cur, patient_id):
    exec_cols = (
        'ekg_id', 'registry_date', 'prob_log_reg', 'prob_rnd_forest', 'prob_log_svm'
    )
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT ekg_id, TO_CHAR(registry_date, 'DD.MM.YYYY HH:MI') as registry_date, "
        f"prob_log_reg, prob_rnd_forest, prob_rnd_forest, prob_log_svm "
        f"FROM ekgs WHERE ekgs.patient_id = {patient_id} "
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
def get_user(conn, cur, login, password):
    cur.execute(
        "SELECT row_to_json(data) FROM "
        "("
        f"SELECT * "
        "FROM users "
        f"WHERE users.login = '{login}' AND users.password = '{password}'"
        ") data"
    )
    data = None
    finding = cur.fetchone()
    if finding is not None:
        data = finding[0]
    return data


@db_transaction
def get_entity(conn, cur, user):
    user_id = user.get('user_id')
    access_level = user.get('access_level')
    if access_level == 1:
        cur.execute(
            "SELECT row_to_json(data) FROM "
            "("
            f"SELECT * "
            "FROM users "
            f"WHERE users.user_id = '{user_id}'"
            ") data"
        )
    elif access_level == 2:
        cur.execute(
            "SELECT row_to_json(data) FROM "
            "("
            f"SELECT * "
            "FROM doctors "
            f"WHERE doctors.user_id = '{user_id}'"
            ") data"
        )
    else:
        cur.execute(
            "SELECT row_to_json(data) FROM "
            "("
            f"SELECT * "
            "FROM patients "
            f"WHERE patients.user_id = '{user_id}'"
            ") data"
        )
    data = None
    finding = cur.fetchone()
    if finding is not None:
        data = finding[0]
    return data


@db_transaction
def delete_patient(conn, cur, patient_id):
    cur.execute(f"SELECT user_id FROM patients WHERE patient_id = {patient_id}")
    user_id = cur.fetchone()[0]
    cur.execute(f"DELETE FROM users WHERE user_id = {user_id}")
    conn.commit()


@db_transaction
def delete_doctor(conn, cur, doctor_id):
    cur.execute(f"SELECT user_id FROM doctors WHERE doctor_id = {doctor_id}")
    user_id = cur.fetchone()[0]
    cur.execute(f"DELETE FROM users WHERE user_id = {user_id}")
    conn.commit()


@db_transaction
def delete_ekg(conn, cur, ekg_id):
    cur.execute(f"DELETE FROM ekgs WHERE ekg_id = {ekg_id}")
    conn.commit()
