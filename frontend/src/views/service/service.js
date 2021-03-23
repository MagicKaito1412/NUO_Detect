import axios from "axios";

const LOCALHOST = 'http://127.0.0.1:5000'
export default {
    loadPatients() {
        return axios.get(`${LOCALHOST}/get_patients`)
    },

    loadDoctors() {
        //todo add after back
    },

    loadEkgs() {
        //todo add after back
    },

    addEkg() {
        //todo add after back
    },

    getPatientsFromCsv() {
        //todo change to form data
        return axios.post(`${LOCALHOST}/export_csv --form filename="D:/Documents/PycharmProjects/NUO_Detect/test_files/test_data_with_unk.csv"`)
    }
}