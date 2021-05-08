import axios from "axios";
import {DB_LOCALHOST} from "./constants";

export default {
    getUserByLoginPassword(login, password) {
        return axios.post(`${DB_LOCALHOST}/get_user`, {
            login: login,
            password: password
        })
    },

    getEntityByUser(user) {
        return axios.post(`${DB_LOCALHOST}/get_entity`, user)
    },
}