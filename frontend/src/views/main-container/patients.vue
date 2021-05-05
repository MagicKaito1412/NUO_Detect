<template>
    <div>
        <h3>Список пациентов, зарегистрированных в системе</h3>
        <n-table :tableData="tableData" :columns="columns"
                 @rowClick="rowClick" @reloadData="reloadData">
            <div class="flr mb-2 justify-sb">
                <n-input label="Фамилия"
                         :value.sync="searchOptions.last_name"/>
                <n-input label="Имя"
                         :value.sync="searchOptions.first_name"/>
                <n-input label="Отчество"
                         :value.sync="searchOptions.middle_name"/>
            </div>
            <template slot="buttons">
                <n-button
                    @click="getPatientsFromCsv"
                    label="Загрузить из CSV"
                />
                <n-button
                    @click="createNew"
                    label="Зарегистрировать пациента"
                />
            </template>
        </n-table>
    </div>
</template>

<script>
import PatientService from '../service/patient-service'
import {PATIENTS_TABLE_HEADERS} from "../service/constants";

export default {
    name: "patients",
    data() {
        return {
            searchOptions: {},
            tableData: []
        }
    },
    methods: {
        loadPatients() {
            PatientService.loadPatients().then(result => {
                this.$set(this, 'tableData', result.data)
            })
        },
        reloadData() {
            PatientService.loadFilteredPatients(this.searchOptions).then(result => {
                this.$set(this, 'tableData', result.data)
            })
        },
        rowClick(item) {
            PatientService.getPatientById(item.patient_id).then(result => {
                this.$store.commit('SET_SELECTED_PATIENT', result.data)
                this.goTo('patient')
            })
        },
        getPatientsFromCsv() {
            PatientService.getPatientsFromCsv().then(result => {
                //todo add file selection later
                console.log('result', result.data)
            })
        },
        createNew() {
            this.$store.commit('SET_SELECTED_PATIENT', {})
            this.goTo('patient', {creationMode: true})
        }
    },
    computed: {
        columns() {
            return Array.from(PATIENTS_TABLE_HEADERS)
        }
    },
    mounted() {
        this.loadPatients()
    }
}
</script>

<style lang="scss">

</style>