<template>
    <div>
        <h3>Врачи, зарегистрированные в системе</h3>
        <n-table :tableData="tableData" :columns="columns"
                 :with-checkbox="true"
                 @handleSelectionChange="handleSelectionChange"
                 @rowClick="rowClick"
                 @reloadData="reloadData">
            <div class="fl-row mb-2 justify-sb">
                <n-input label="Фамилия"
                         @keyup.enter.native.prevent="reloadData"
                         :value.sync="searchOptions.last_name"/>
                <n-input label="Имя"
                         @keyup.enter.native.prevent="reloadData"
                         :value.sync="searchOptions.first_name"/>
                <n-input label="Отчество"
                         @keyup.enter.native.prevent="reloadData"
                         :value.sync="searchOptions.middle_name"/>
            </div>
            <template slot="buttons">
                <n-button
                    @click="createNew"
                    label="Зарегистировать нового"/>
                <n-button
                    :disabled="disableClearButton"
                    @click="resetSearchOptions"
                    label="Очистить"
                />
                <n-button
                    :disabled="disableRemoveButton"
                    type="error"
                    @click="removeList"
                    label="Удалить из системы"
                />
            </template>
        </n-table>
        <doctor-editor :visible.sync="showDialog"
                       :createMode.sync="createMode"
                       :showLoginDialog.sync="showLoginDialog"
                       :newUserLogin.sync="newUserLogin"
                       @reloadData="reloadData"/>
        <n-text-dialog :visible.sync="showLoginDialog"
                       :text="loginDialogText"/>
    </div>
</template>

<script>
import Service from './doctor-service'
import {DOCTORS_TABLE_HEADERS} from "../../service/constants";
import DoctorEditor from './doctor-editor'

export default {
    name: "doctors",
    components: {DoctorEditor},
    data() {
        return {
            searchOptions: {},
            tableData: [],
            showDialog: false,
            showLoginDialog: false,
            createMode: false,
            checked: [],
            newUserLogin: null
        }
    },
    methods: {
        loadDoctors() {
            this.$store.commit('SET_PROGRESS', true)
            Service.loadDoctors().then(result => {
                this.$set(this, 'tableData', result.data)
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        reloadData() {
            this.$store.commit('SET_PROGRESS', true)
            Service.loadFilteredDoctors(this.searchOptions).then(result => {
                this.$set(this, 'tableData', result.data)
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        rowClick(item) {
            Service.getDoctorById(item.doctor_id).then(result => {
                if (result) {
                    this.$store.commit('SET_SELECTED_DOCTOR', result.data)
                    this.$set(this, 'showDialog', true)
                }
            })
        },
        createNew() {
            this.$set(this, 'createMode', true)
            this.$set(this, 'showDialog', true)
        },
        resetSearchOptions() {
            this.$set(this, 'searchOptions', {})
        },
        handleSelectionChange(checked) {
            this.$set(this, 'checked', checked)
        },
        removeList() {
            //todo after back
        }
    },
    computed: {
        columns() {
            return Array.from(DOCTORS_TABLE_HEADERS)
        },
        disableClearButton() {
            return !this.searchOptions.last_name
            && !this.searchOptions.first_name
            && !this.searchOptions.middle_name
        },
        disableRemoveButton() {
            return !this.checked || !this.checked.length
        },
        loginDialogText() {
            if (this.newUserLogin) {
                return `Для пользователя зарегистирован логин: ${this.newUserLogin}`
            }
            return ''
        }
    },
    mounted() {
        this.loadDoctors()
    }
}
</script>

<style scoped>

</style>