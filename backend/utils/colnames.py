ID = 'Номер пациента пациент'
FIO = 'ФИО'
TYPE = 'пол (1 - мужской, 2-женский)'
AGE = 'age'
WEIGHT = 'вес'
HEIGHT = 'рост'
PROB_LOG_REG = 'Вероятность модели (log_reg)'
PROB_RND_FOREST = 'Вероятность модели (randrom_forest)'
PROB_SVM = 'Вероятность модели (svm)'

ECG = 'номер ЭКГ'
DATE = 'Дата/Время съема ЭКГ/глюкозы'

NOISY_COLS = ['qt', 'st', 'P', 'pq', 'qrs', 'p_left_slopes', 'p_right_slopes',
              'q_left_slopes', 'q_right_slopes', 't_left_slopes', 't_right_slopes']
USELESS_COLS = [ID, 'номер ЭКГ', 'Дата рождения', 'Дата/Время съема ЭКГ/глюкозы', 'комментарий']
DISRESPECT_COLS = ['Натощак']
TARGET_COL = 'Площадка исследования ("1" - с диабетом 2 типа, "0","2","3","4" - без диабета)'

COLUMN_MAP = {
    'номер ЭКГ': 'Номер ЭКГ',
    'Дата/Время съема ЭКГ/глюкозы': 'Дата/Время съема ЭКГ',
    'sdnn': 'Cтандартное отклонение NN-интервалов (SDNN)',
    'skewness': 'Коэффициент асимметрии NN-интервалов (Skewness)',
    'Amo': 'Амплитуда моды NN-интервалов (AMo)',
    'SWAI': 'Индекс медленноволновой аритмии (SWAI)',
    'Mo': 'Мода NN –интервалов по кардиоинтевалограмме с шагом 100мс (Mo)',
    'dRR': 'Вариационный размах RR-интервалов (dRR)',
    'RRNN': 'Средняя длительность NN-интервалов (RRNN)',
    'pNN50': ('Доля пар последовательных NN-интервалов, различающихся более, '
              'чем на 50 мс среди всех NN-интервалов (pNN50)'),
    'SI': 'Индекс напряжения (SI)',
    'SATI': 'Индекс симпато-адреналового тонуса (SATI)',
    'RMI': 'Индекс дыхательной модуляции (RMI)',
    'kurtosis': 'Коэффициент эксцесса NN-интервалов (Kurtosis)',
    'CV': 'Коэффициент вариации NN-интервалов (CV)',
    'RMSSD': 'Среднеквадратичное различие между продолжительностью соседних NN-интервалов (RMSSD)',
    'NN50': 'Количество пар последовательных NN-интервалов, различающихся более, чем на 50 мс (NN50)',
    'lf': 'Мощность ВСР в диапазоне низких частот (LF)',
    'lfhf': 'Отношение мощности в диапазоне низких частот к мощности в диапазоне высоких частот (LF/HF)',
    'hfp': 'Отношение мощности в диапазоне высоких частот к общей мощности (HFp=HF/TP)',
    'ulf': 'Мощность ВСР в диапазоне ультранизких частот (ULF)',
    'tp': 'Общая мощность ВСР (TP=VLF+LF+HF)',
    'vlf': 'Мощность ВСР в диапазоне очень низких частот (VLF)',
    'vlfp': 'Отношение мощности в диапазоне очень низких частот к общей мощности (VLFp=VLF/TP)',
    'lfp': 'Отношение мощности в диапазоне низких частот к общей мощности (LFp=LF/TP)',
    'br': 'Частота дыхания (BR)',
    'ulfp': 'Отношение мощности в диапазоне ультранизких частот к общей мощности (ULFp=ULF/TP)',
    'ic': 'Индекс централизации (IC)',
    'hf': 'Мощность ВСР в диапазоне высоких частот (HF)',
    'tpfull': 'Другая общая мощность ВСР (TPfull=ULF+VLF+LF+HF)',
    'p_left_slopes': 'Левый склон P-зубца',
    'p_right_slopes': 'Правый склон P-зубца',
    'q_left_slopes': 'Левый склон Q-зубца',
    'q_right_slopes': 'Правый склон Q-зубца',
    't_left_slopes': 'Левый склон T-зубца',
    't_right_slopes': 'Правый склон T-зубца',
    'qt': 'Ширина интервала QT',
    'st': 'Ширина сегмента ST',
    'P': 'Ширина P-зубца',
    'pq': 'Ширина PQ-интервала',
    'qrs': 'Ширина QRS-комплекса',
    'pulse': 'ЧСС (число ударов в секунду)'
}


DB_PROB_LOG_REG = 'prob_log_reg'
DB_PROB_RND_FOREST = 'prob_log_svm'
DB_PROB_SVM = 'prob_rnd_forest'
DB_PATIENT_ID = 'patient_id'
DB_EKG_USELESS_COLS = ['ekg_id', 'patient_id', 'registry_date', 'prob_log_reg', 'prob_log_svm', 'prob_rnd_forest']
DB_TARGET_COL = 'has_nuo'
DB_REGISTRY_DATE = 'registry_date'
EKG_COLUMNS = [
    'ekg_id',
    'patient_id',
    'registry_date',
    'sdnn',
    'skewness',
    'Amo',
    'SWAI',
    'Mo',
    'dRR',
    'RRNN',
    'pNN50',
    'SI',
    'SATI',
    'RMI',
    'kurtosis',
    'CV',
    'RMSSD',
    'NN50',
    'lf',
    'lfhf',
    'hfp',
    'ulf',
    'tp',
    'vlf',
    'vlfp',
    'lfp',
    'br',
    'ulfp',
    'ic',
    'hf',
    'tpfull',
    'p_left_slopes',
    'p_right_slopes',
    'q_left_slopes',
    'q_right_slopes',
    't_left_slopes',
    't_right_slopes',
    'qt',
    'st',
    'P',
    'pq',
    'qrs',
    'pulse',
    'has_nuo',
    'prob_log_reg',
    'prob_rnd_forest',
    'prob_log_svm'
]
