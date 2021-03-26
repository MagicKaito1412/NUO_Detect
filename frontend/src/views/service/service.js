import axios from "axios";

const LOCALHOST = 'http://127.0.0.1:5000'
const CONFIG = {
    headers: {
        'Content-Type': 'application/json',
    }
}
export default {
    //patients
    getPatientById(id) {
        return axios.get(`${LOCALHOST}/get_patient/${id}`)
    },

    loadPatients() {
        return axios.get(`${LOCALHOST}/get_all_patients`)
    },

    loadFilteredPatients(filters) {
        return axios.post(`${LOCALHOST}/get_patients`, filters, CONFIG)
    },

    saveNewPatient(dto) {
        return axios.post(`${LOCALHOST}/insert_patient`, dto, CONFIG)
    },

    updatePatient(dto) {
        return axios.post(`${LOCALHOST}/update_patient`, dto, CONFIG)
    },

    getPatientsFromCsv() {
        //todo change to form data
        return axios.post(`${LOCALHOST}/export_csv --form filename="D:/Documents/PycharmProjects/NUO_Detect/test_files/test_data_with_unk.csv"`)
    },

    //doctors
    loadDoctors() {
        //todo add after back
    },


    //load ekg
    loadEkgs(patient_id) {
         return axios.get(`${LOCALHOST}/get_patient_ekgs/${patient_id}`)
        //todo add after back
    },

    addEkg(dto) {
        return axios.post(`${LOCALHOST}/insert_ekg`, dto, CONFIG)
    },
}