import axios from "axios";
import {DB_LOCALHOST} from "./constants";

export default {
    getUserById(user_id) {
        return axios.get(`${DB_LOCALHOST}/get_user/${user_id}`)
    },

    getUserByLoginPassword(login, password) {
        return axios.post(`${DB_LOCALHOST}/get_user`, {
            login: login,
            password: password
        })
    },

    getEntityByUser(user) {
        return axios.post(`${DB_LOCALHOST}/get_entity`, user)
    },

    changePassword(user) {
        return axios.post(`${DB_LOCALHOST}/update_user`, user)
    }
}