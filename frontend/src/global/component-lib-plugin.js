import CardioLogoGenerator from './components/cardio-logo-generator'
import MainWrapper from './components/main-wrapper'
import Divider from './components/divider'
import NDialog from './components/n-dialog'
import NTable from './components/n-table'
import NInput from './components/n-input'
import NButton from './components/n-button'
import NLoader from './components/n-loader'
import NDatePicker from './components/n-date-picker'
import NTimePicker from './components/n-time-picker'
import NSubHeader from './components/n-sub-header'

export default {
    install(Vue) {
        Vue.component(CardioLogoGenerator.name, CardioLogoGenerator)
        Vue.component(MainWrapper.name, MainWrapper)
        Vue.component(Divider.name, Divider)
        Vue.component(NDialog.name, NDialog)
        Vue.component(NTable.name, NTable)
        Vue.component(NInput.name, NInput)
        Vue.component(NButton.name, NButton)
        Vue.component(NLoader.name, NLoader)
        Vue.component(NDatePicker.name, NDatePicker)
        Vue.component(NTimePicker.name, NTimePicker)
        Vue.component(NSubHeader.name, NSubHeader)
    }
}