import ComponentLib from './component-lib-plugin'
import ElementUiLib from './element-ui-plugin'
import MixinLib from './mixin-lib-plugin'

export default {
    install(Vue, opt) {
        Vue.use(ComponentLib, opt);
        Vue.use(ElementUiLib, opt);
        Vue.use(MixinLib, opt);
    }
}