import ComponentLib from './plugins/component-lib-plugin'
import ElementUiLib from './plugins/element-ui-plugin'
import MixinLib from './plugins/mixin-lib-plugin'
import VueChartLib from './plugins/vue-chart-plugin'

export default {
    install(Vue, opt) {
        Vue.use(ComponentLib, opt);
        Vue.use(ElementUiLib, opt);
        Vue.use(MixinLib, opt);
        Vue.use(VueChartLib, opt);
    }
}