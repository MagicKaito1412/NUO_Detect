import Vue from "vue";
import Vuex from "vuex";
import VuexPersist from "vuex-persist";

Vue.use(Vuex)

const vuexSessionStorage = new VuexPersist({
    key: "vuex",
    storage: window.sessionStorage,
});

const state = {
    authUser: {}, //class User
    authPerson: {}, //class User or Doctor or Patient
    selectedPatient: {}, //class Patient
    selectedDoctor: {}, //class Doctor
};

const getters = {
    getAuthUser: state => state.authUser,
    getAuthPerson: state => state.authPerson,
    getSelectedPatient: state => state.selectedPatient,
    getSelectedDoctor: state => state.selectedDoctor,
};

const mutations = {
    SET_AUTH_USER(state, value) {
        state.authUser = value
    },
    SET_AUTH_PERSON(state, value) {
        state.authPerson = value
    },
    SET_SELECTED_PATIENT(state, value) {
        state.selectedPatient = value
    },
    SET_SELECTED_DOCTOR(state, value) {
        state.selectedDoctor = value
    },
    LOGOUT(state) {
        state.authUser = {}
        state.authPerson = {}
        state.selectedPatient = {}
        state.selectedDoctor = {}
    }
};

const actions = {};

export default new Vuex.Store({
    plugins: [vuexSessionStorage.plugin],
    state,
    getters,
    mutations,
    actions,
    strict: true
});