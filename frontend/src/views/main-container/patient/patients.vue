<template>
    <div>
        <h3 class="mt-0 mb-10">Список пациентов, зарегистрированных в системе</h3>
        <n-table :tableData="tableData" :columns="columns"
                 @rowClick="rowClick" @reloadData="reloadData">
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
                <input
                    accept=".csv"
                    @change="selectFile"
                    ref="fileInput"
                    style="display:none;"
                    type="file"
                />
                <n-button @click="$refs.fileInput.click()"
                          label="Загрузить из CSV"/>
                <n-button
                    @click="createNew"
                    label="Зарегистрировать пациента"
                />
                <n-button
                    :disabled="disableClearButton"
                    @click="resetSearchOptions"
                    label="Очистить"
                />
            </template>
        </n-table>
    </div>
</template>

<script>
import PatientService from './patient-service'
import {PATIENTS_TABLE_HEADERS} from "../../service/constants";

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
            this.$store.commit('SET_PROGRESS', true)
            PatientService.loadPatients().then(result => {
                this.$set(this, 'tableData', result.data)
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        reloadData() {
            this.$store.commit('SET_PROGRESS', true)
            PatientService.loadFilteredPatients(this.searchOptions).then(result => {
                this.$set(this, 'tableData', result.data)
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        rowClick(item) {
            this.$store.commit('SET_PROGRESS', true)
            PatientService.getPatientById(item.patient_id).then(result => {
                this.$store.commit('SET_SELECTED_PATIENT', result.data)
                this.goTo('patient', {creationMode: false})
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        selectFile(event) {
            this.getPatientsFromCsv(event.target.files);
            this.$nextTick(() => {
                if (this.$refs.fileInput) {
                    this.$refs.fileInput.value = null;
                }
            });
        },
        getPatientsFromCsv(files) {
            let file = files[0]
            this.$store.commit('SET_PROGRESS', true)
            PatientService.getPatientsFromCsv(file).then(() => {
                this.reloadData()
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        createNew() {
            this.$store.commit('SET_SELECTED_PATIENT', {})
            this.goTo('patient', {creationMode: true})
        },
        resetSearchOptions() {
            this.$set(this, 'searchOptions', {})
        }
    },
    computed: {
        columns() {
            return Array.from(PATIENTS_TABLE_HEADERS)
        },
        disableClearButton() {
            return !this.searchOptions.last_name
                && !this.searchOptions.first_name
                && !this.searchOptions.middle_name
        }
    },
    mounted() {
        this.loadPatients()
    }
}
</script>

<style lang="scss">

</style>