import Vue from "vue";
import Vuex from "vuex";
import VuexPersist from "vuex-persist";

Vue.use(Vuex)

const vuexSessionStorage = new VuexPersist({
    key: "vuex",
    storage: window.sessionStorage,
});

const state = {};

const getters = {};

const mutations = {};

const actions = {};

export default new Vuex.Store({
    plugins: [vuexSessionStorage.plugin],
    state,
    getters,
    mutations,
    actions,
    strict: true
});