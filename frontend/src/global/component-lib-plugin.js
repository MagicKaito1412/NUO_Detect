import CardioLogoGenerator from './components/cardio-logo-generator'
import MainWrapper from './components/main-wrapper'
import Divider from './components/divider'

export default {
    install(Vue) {
        Vue.component(CardioLogoGenerator.name, CardioLogoGenerator)
        Vue.component(MainWrapper.name, MainWrapper)
        Vue.component(Divider.name, Divider)
    }
}