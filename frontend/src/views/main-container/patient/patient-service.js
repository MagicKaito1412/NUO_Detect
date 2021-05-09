import axios from "axios";
import {CONFIG, DB_LOCALHOST, PREDICT_LOCALHOST} from "../../service/constants";

export default {
    getPatientById(id) {
        return axios.get(`${DB_LOCALHOST}/get_patient/${id}`)
    },

    loadPatients() {
        return axios.get(`${DB_LOCALHOST}/get_all_patients`)
    },

    loadPatientStatistics() {
        return axios.get(`${DB_LOCALHOST}/get_stat`)
    },

    loadFilteredPatients(filters) {
        return axios.post(`${DB_LOCALHOST}/get_patients`, filters, CONFIG)
    },

    saveNewPatient(dto) {
        return axios.post(`${DB_LOCALHOST}/insert_patient`, dto, CONFIG)
    },

    updatePatient(dto) {
        return axios.post(`${DB_LOCALHOST}/update_patient`, dto, CONFIG)
    },

    getPatientsFromCsv(file) {
        let formData = new FormData()
        formData.append("file", file)
        return axios.post(`${DB_LOCALHOST}/export_csv`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
    },

    predict(patient_id) {
        return axios.post(`${PREDICT_LOCALHOST}/predict/${patient_id}`)
    },
}