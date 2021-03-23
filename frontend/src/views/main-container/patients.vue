<template>
    <div>
        <h3>Список пациентов, зарегистрированных в системе</h3>
        <n-table :tableData="tableData" :columns="columns" @rowClick="rowClick">
            <div class="flr mb-2 justify-sb">
                <n-input label="Фамилия"
                         :value.sync="searchOptions.last_name"/>
                <n-input label="Имя"
                         :value.sync="searchOptions.first_name"/>
                <n-input label="Отчество"
                         :value.sync="searchOptions.middle_name"/>
                <n-input label="Номер полиса"
                         :value.sync="searchOptions.policy_num"/>
            </div>
            <template slot="buttons">
                <el-button @click="getPatientsFromCsv">Загрузить из CSV</el-button>
                <el-button @click="createNew">Зарегистрировать пациента</el-button>
            </template>
        </n-table>
    </div>
</template>

<script>
import Service from '../service/service'
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
            Service.loadPatients().then(result => {
                this.$set(this, 'tableData', result.data)
            })
        },
        rowClick(item) {
            //todo mb get patient by id
            this.$store.commit('SET_SELECTED_PATIENT', item)
            this.goTo('patient')
        },
        getPatientsFromCsv() {
            Service.getPatientsFromCsv().then(result => {
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