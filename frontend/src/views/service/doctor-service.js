import {CONFIG, LOCALHOST} from "./constants";
import axios from "axios";

export default {

    loadDoctors() {
        return axios.get(`${LOCALHOST}/get_all_doctors`)
    },

    loadFilteredDoctors(filters) {
        return axios.post(`${LOCALHOST}/get_doctors`, filters, CONFIG)
    },

    getDoctorById() {
        // return axios.get(`${LOCALHOST}/get_doctor/${id}`)
        //todo add after back
    },

    saveNewDoctor(dto) {
        return axios.post(`${LOCALHOST}/insert_doctor`, dto, CONFIG)
    },

    updateDoctor(dto) {
         return axios.post(`${LOCALHOST}/update_doctor`, dto, CONFIG)
    },
}