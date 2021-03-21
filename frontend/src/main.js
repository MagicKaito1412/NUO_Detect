import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import moment from "moment";
import GlobalLibPlugin from './global/global-lib-plugin'
import '@/assets/scss/index.scss';

Vue.config.productionTip = false
moment.locale("ru");

Vue.use(GlobalLibPlugin, {
    store: store,
    router: router
});

const app = new Vue({
    render: h => h(App),
    router,
    store
}).$mount('#app');

export {app}
