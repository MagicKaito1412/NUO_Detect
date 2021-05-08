import axios from "axios";
import {CONFIG, DB_LOCALHOST} from "../../service/constants";

export default {
    loadEkgs(patient_id) {
         return axios.get(`${DB_LOCALHOST}/get_patient_ekgs/${patient_id}`)
    },

    saveNewEkg(dto) {
        return axios.post(`${DB_LOCALHOST}/insert_ekg`, dto, CONFIG)
    },

    updateEkg(dto) {
        return axios.post(`${DB_LOCALHOST}/update_ekg`, dto, CONFIG)
    },

    getEkgById(ekg_id) {
        return axios.get(`${DB_LOCALHOST}/get_ekg/${ekg_id}`)
    },
}