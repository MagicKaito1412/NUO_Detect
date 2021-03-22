import CardioLogoGenerator from './components/cardio-logo-generator'
import MainWrapper from './components/main-wrapper'
import Divider from './components/divider'
import NDialog from './components/n-dialog'

export default {
    install(Vue) {
        Vue.component(CardioLogoGenerator.name, CardioLogoGenerator)
        Vue.component(MainWrapper.name, MainWrapper)
        Vue.component(Divider.name, Divider)
        Vue.component(NDialog.name, NDialog)
    }
}