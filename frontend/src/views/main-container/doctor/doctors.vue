<template>
    <div>
        <h3>Врачи, зарегистрированные в системе</h3>
        <n-table :tableData="tableData" :columns="columns"
                 :with-checkbox="true"
                 @handleSelectionChange="handleSelectionChange"
                 @rowClick="rowClick"
                 @reloadData="reloadData">
            <div class="flr mb-2 justify-sb">
                <n-input label="Фамилия"
                         @keyup.enter.native.prevent="reloadData"
                         :value.sync="searchOptions.last_name"/>
                <n-input label="Имя"
                         @keyup.enter.native.prevent="reloadData"
                         :value.sync="searchOptions.first_name"/>
                <n-input label="Отчество"
                         @keyup.enter.native.prevent="reloadData"
                         :value.sync="searchOptions.middle_name"/>
                <n-input label="Номер телефона"
                         mask="###########"
                         @keyup.enter.native.prevent="reloadData"
                         :value.sync="searchOptions.telephone"/>
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
                       @reloadData="reloadData"/>
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
            createMode: false,
            checked: []
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
            && !this.searchOptions.telephone //todo change to cabinet
        },
        disableRemoveButton() {
            return !this.checked || !this.checked.length
        },
    },
    mounted() {
        this.loadDoctors()
    }
}
</script>

<style scoped>

</style>