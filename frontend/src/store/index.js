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
    authEntity: {}, //class User or Doctor or Patient
    selectedPatient: {}, //class Patient
    selectedDoctor: {}, //class Doctor
    selectedEkg: {}, //class Ekg
    progress: false
};

const getters = {
    getAuthUser: state => state.authUser,
    getAuthEntity: state => state.authEntity,
    getSelectedPatient: state => state.selectedPatient,
    getSelectedDoctor: state => state.selectedDoctor,
    getSelectedEkg: state => state.selectedEkg,
    getProgress: state => state.progress
};

const mutations = {
    SET_AUTH_USER(state, value) {
        state.authUser = value
    },
    SET_AUTH_ENTITY(state, value) {
        state.authEntity = value
    },
    SET_SELECTED_PATIENT(state, value) {
        state.selectedPatient = value
    },
    SET_SELECTED_DOCTOR(state, value) {
        state.selectedDoctor = value
    },
    SET_SELECTED_EKG(state, value) {
        state.selectedEkg = value
    },
    LOGOUT(state) {
        state.authUser = {}
        state.authEntity = {}
        state.selectedPatient = {}
        state.selectedDoctor = {}
        state.selectedEkg = {}
    },
    SET_PROGRESS(state, value) {
        state.progress = value
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