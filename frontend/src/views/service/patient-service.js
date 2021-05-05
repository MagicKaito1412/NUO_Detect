import axios from "axios";
import {CONFIG, LOCALHOST} from "./constants";

export default {
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

    getPatientsFromCsv(file) {
        let formData = new FormData()
        formData.append("file", file)
        return axios.post(`${LOCALHOST}/export_csv`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
    },
}