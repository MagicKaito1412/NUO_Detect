import {CONFIG, DB_LOCALHOST} from "../../service/constants";
import axios from "axios";

export default {

    loadDoctors() {
        return axios.get(`${DB_LOCALHOST}/get_all_doctors`)
    },

    loadFilteredDoctors(filters) {
        return axios.post(`${DB_LOCALHOST}/get_doctors`, filters, CONFIG)
    },

    getDoctorById(doctor_id) {
        return axios.get(`${DB_LOCALHOST}/get_doctor/${doctor_id}`)
    },

    saveNewDoctor(dto) {
        return axios.post(`${DB_LOCALHOST}/insert_doctor`, dto, CONFIG)
    },

    updateDoctor(dto) {
         return axios.post(`${DB_LOCALHOST}/update_doctor`, dto, CONFIG)
    },

    deleteDoctor(doctor_id) {
         return axios.delete(`${DB_LOCALHOST}/delete_doctor/${doctor_id}`)
    },
}