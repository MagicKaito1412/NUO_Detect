import Vue from "vue";
import Vuex from "vuex";
import VuexPersist from "vuex-persist";

Vue.use(Vuex)

const vuexSessionStorage = new VuexPersist({
    key: "vuex",
    storage: window.sessionStorage,
});

const state = {
    authUser: {},
    authPerson: {},
};

const getters = {
    getAuthUser: state => state.authUser,
    getAuthPerson: state => state.authPerson,
};

const mutations = {
    SET_AUTH_USER(state, value) {
        state.authUser = value
    },
    SET_AUTH_PERSON(state, value) {
        state.authPerson = value
    },
    LOGOUT(state) {
        state.authUser = {}
        state.authPerson = {}
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