import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import moment from "moment";

Vue.config.productionTip = false
moment.locale("ru");

const app = new Vue({
    render: h => h(App),
    router,
    store
}).$mount('#app');

export {app}
