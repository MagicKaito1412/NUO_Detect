from sqlalchemy.dialects.postgresql import *
from backend.db_module.entities.common_entity import CoreEntity
from backend.db_module.app import db

SCHEMA = 'public'


class User(CoreEntity):
    __table_args__ = ({"schema": SCHEMA})
    __tablename__ = "users"

    id = db.Column(name='user_id', type_=BIGINT, unique=True, primary_key=True, nullable=False)
    login = db.Column(name='login', type_=VARCHAR(30), unique=True, nullable=False)
    password = db.Column(name='password', type_=VARCHAR(50), nullable=False)
    access_level = db.Column(name='access_level', type_=INTEGER, nullable=False)


class Patient(CoreEntity):
    __table_args__ = ({"schema": SCHEMA})
    __tablename__ = "patients"

    id = db.Column(name='patient_id', type_=BIGINT, unique=True, primary_key=True, nullable=False)
    user_id = db.Column(name='user_id', type_=BIGINT, unique=True, nullable=False)
    first_name = db.Column(name='first_name', type_=VARCHAR(30), nullable=False)
    last_name = db.Column(name='last_name', type_=VARCHAR(50), nullable=False)
    middle_name = db.Column(name='middle_name', type_=VARCHAR(50))
    gender = db.Column(name='gender', type_=INTEGER, nullable=False)
    age = db.Column(name='age', type_=INTEGER, nullable=False)
    weight = db.Column(name='weight', type_=INTEGER, nullable=False)
    height = db.Column(name='height', type_=INTEGER, nullable=False)
    has_nuo = db.Column(name='has_nuo', type_=BOOLEAN)
    prob_log_reg = db.Column(name='prob_log_reg', type_=REAL, nullable=False)
    prob_rnd_forest = db.Column(name='prob_rnd_forest', type_=REAL, nullable=False)
    prob_log_svm = db.Column(name='prob_log_svm', type_=REAL, nullable=False)


class Doctor(CoreEntity):
    __table_args__ = ({"schema": SCHEMA})
    __tablename__ = "doctors"

    id = db.Column(name='doctor_id', type_=BIGINT, unique=True, primary_key=True, nullable=False)
    user_id = db.Column(name='user_id', type_=BIGINT, unique=True, nullable=False)
    full_name = db.Column(name='full_name', type_=VARCHAR(150), nullable=False)
    cabinet = db.Column(name='cabinet', type_=REAL)
    telephone = db.Column(name='telephone', type_=INTEGER, nullable=False)


class EKG(CoreEntity):
    __table_args__ = ({"schema": SCHEMA})
    __tablename__ = "ekgs"

    id = db.Column(name='ekg_id', type_=BIGINT, unique=True, primary_key=True, nullable=False)
    patient_id = db.Column(name='patient_id', type_=BIGINT, nullable=False)
    date = db.Column(name='date', type_=DATE, nullable=False)  # Дата/Время съема ЭКГ
    sdnn = db.Column(name='sdnn', type_=FLOAT)  # Cтандартное отклонение NN-интервалов (SDNN)
    skewness = db.Column(name='skewness', type_=FLOAT)  # Коэффициент асимметрии NN-интервалов (Skewness)
    amo = db.Column(name='amo', type_=FLOAT)  # Амплитуда моды NN-интервалов (AMo)
    swai = db.Column(name='swai', type_=FLOAT)  # Индекс медленноволновой аритмии (SWAI)
    mo = db.Column(name='mo', type_=FLOAT)  # Мода NN –интервалов по кардиоинтевалограмме с шагом 100мс (Mo)
    drr = db.Column(name='drr', type_=FLOAT)  # Вариационный размах RR-интервалов (dRR)
    rrnn = db.Column(name='rrnn', type_=FLOAT)  # Средняя длительность NN-интервалов (RRNN)
    pnn50 = db.Column(name='pnn50',
                      type_=FLOAT)  # Доля пар последовательных NN-интервалов, различающихся более, чем на 50 мс среди
                                    # всех NN-интервалов (pNN50)
    si = db.Column(name='si', type_=FLOAT)  # Индекс напряжения (SI)
    sati = db.Column(name='sati', type_=FLOAT)  # Индекс симпато-адреналового тонуса (SATI)
    rmi = db.Column(name='rmi', type_=FLOAT)  # 'Индекс дыхательной модуляции (RMI)
    kurtosis = db.Column(name='kurtosis', type_=FLOAT)  # Коэффициент эксцесса NN-интервалов (Kurtosis)
    cv = db.Column(name='cv', type_=FLOAT)  # Коэффициент вариации NN-интервалов (CV)
    rmssd = db.Column(name='rmssd',
                      type_=FLOAT)  # Среднеквадратичное различие между продолжительностью соседних NN-интервалов
                                    # (RMSSD)
    nn50 = db.Column(name='nn50',
                     type_=FLOAT)  # Количество пар последовательных NN-интервалов, различающихся более, чем на 50 мс
                                    # (NN50)
    lf = db.Column(name='lf', type_=FLOAT)  # Мощность ВСР в диапазоне низких частот (LF)
    lfhf = db.Column(name='lfhf',
                     type_=FLOAT)  # Отношение мощности в диапазоне низких частот к мощности в диапазоне высоких частот
                                    # (LF/HF)
    hfp = db.Column(name='hfp',
                    type_=FLOAT)  # Отношение мощности в диапазоне высоких частот к общей мощности (HFp=HF/TP)
    ulf = db.Column(name='ulf', type_=FLOAT)  # Мощность ВСР в диапазоне ультранизких частот (ULF)
    tp = db.Column(name='tp', type_=FLOAT)  # Общая мощность ВСР (TP=VLF+LF+HF)
    vlf = db.Column(name='vlf', type_=FLOAT)  # Мощность ВСР в диапазоне очень низких частот (VLF)
    vlfp = db.Column(name='vlfp',
                     type_=FLOAT)  # Отношение мощности в диапазоне очень низких частот к общей мощности (VLFp=VLF/TP)
    lfp = db.Column(name='lfp',
                    type_=FLOAT)  # Отношение мощности в диапазоне низких частот к общей мощности (LFp=LF/TP)
    br = db.Column(name='br', type_=FLOAT)  # Частота дыхания (BR)
    ulfp = db.Column(name='ulfp',
                     type_=FLOAT)  # Отношение мощности в диапазоне ультранизких частот к общей мощности (ULFp=ULF/TP)
    ic = db.Column(name='ic', type_=FLOAT)  # Индекс централизации (IC)
    hf = db.Column(name='hf', type_=FLOAT)  # Мощность ВСР в диапазоне высоких частот (HF)
    tpfull = db.Column(name='tpfull', type_=FLOAT)  # Другая общая мощность ВСР (TPfull=ULF+VLF+LF+HF)
    p_left_slopes = db.Column(name='p_left_slopes', type_=FLOAT)  # Левый склон P-зубца
    p_right_slopes = db.Column(name='p_right_slopes', type_=FLOAT)  # Правый склон P-зубца
    q_left_slopes = db.Column(name='q_left_slopes', type_=FLOAT)  # Левый склон Q-зубца
    q_right_slopes = db.Column(name='q_right_slopes', type_=FLOAT)  # Правый склон Q-зубца
    t_left_slopes = db.Column(name='t_left_slopes', type_=FLOAT)  # Левый склон T-зубца
    t_right_slopes = db.Column(name='t_right_slopes', type_=FLOAT)  # Правый склон T-зубца
    qt = db.Column(name='qt', type_=FLOAT)  # Ширина интервала QT
    st = db.Column(name='st', type_=FLOAT)  # Ширина сегмента ST
    p = db.Column(name='p', type_=FLOAT)  # Ширина P-зубца
    pq = db.Column(name='pq', type_=FLOAT)  # Ширина PQ-интервала
    qrs = db.Column(name='qrs', type_=FLOAT)  # Ширина QRS-комплекса
    pulse = db.Column(name='pulse', type_=INTEGER)  # pulse(число ударов в секунду)
