import axios from "axios";
import {LOCALHOST} from "./constants";

export default {
    getUserByLoginPassword(login, password) {
        return axios.post(`${LOCALHOST}/get_user`, {
            login: login,
            password: password
        })
    },

    // getEntityByUser(user) {
    //     //todo for all
    // },
}