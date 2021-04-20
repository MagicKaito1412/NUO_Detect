import axios from "axios";
import {CONFIG, LOCALHOST} from "./constants";

export default {
    loadEkgs(patient_id) {
         return axios.get(`${LOCALHOST}/get_patient_ekgs/${patient_id}`)
        //todo add after back
    },

    addEkg(dto) {
        return axios.post(`${LOCALHOST}/insert_ekg`, dto, CONFIG)
    },
}