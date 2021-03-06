export const DB_LOCALHOST = 'http://127.0.0.1:5000'
export const TRAIN_LOCALHOST = 'http://127.0.0.1:5010'
export const PREDICT_LOCALHOST = 'http://127.0.0.1:5015'
export const REPORT_LOCALHOST = 'http://127.0.0.1:5020'

export const CONFIG = {
    headers: {
        'Content-Type': 'application/json',
    }
}

export const TELEPHONE_PATTERN = '+ 7 (###) ###-##-##'
export const POLICY_PATTERN = '#### #### #### ####'

export const PATIENTS_TABLE_HEADERS = [
    {
        title: "НОМЕР ПАЦИЕНТА",
        key: "patient_id",
    },{
        title: "ФАМИЛИЯ",
        key: "last_name",
    },{
        title: "ИМЯ",
        key: "first_name",
    },{
        title: "ОТЧЕСТВО",
        key: "middle_name",
    },{
        title: "ВОЗРАСТ",
        key: "age",
    },{
        title: "НОМЕР ПОЛИСА ОМС",
        key: "policy_num",
    },
]

export const DOCTORS_TABLE_HEADERS = [
    {
        title: "НОМЕР ВРАЧА",
        key: "doctor_id",
    },{
        title: "ФАМИЛИЯ",
        key: "last_name",
    },{
        title: "ИМЯ",
        key: "first_name",
    },{
        title: "ОТЧЕСТВО",
        key: "middle_name",
    },{
        title: "ТЕЛЕФОН",
        key: "telephone",
    }
]

export const EKGS_TABLE_HEADERS = [
    {
        title: "НОМЕР ЭКГ",
        key: "ekg_id",
    },{
        title: "ДАТА И ВРЕМЯ СЪЕМА",
        key: "registry_date",
    }
]

export const PROBS_EKGS_TABLE_HEADERS = [
    {
        title: "LOG REG",
        key: "prob_log_reg",
    },{
        title: "RANDOM FOREST",
        key: "prob_rnd_forest",
    },{
        title: "SVM",
        key: "prob_log_svm",
    },
]