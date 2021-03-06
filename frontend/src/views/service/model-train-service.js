import axios from "axios";
import {TRAIN_LOCALHOST} from "./constants";

export default {
    train() {
        return axios.post(`${TRAIN_LOCALHOST}/train`)
    },

    calcSensSpec() {
        return axios.get(`${TRAIN_LOCALHOST}/calc_sens_spec`)
    },

    getSensSpec() {
        return axios.get(`${TRAIN_LOCALHOST}/get_sens_spec`)
    },
}