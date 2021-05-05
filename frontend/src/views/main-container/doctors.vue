<template>
    <div>
        <h3>Врачи, зарегистрированные в системе</h3>
        <n-table :tableData="tableData" :columns="columns"
                 @rowClick="rowClick" @reloadData="reloadData">
            <div class="flr mb-2 justify-sb">
                <n-input label="Фамилия"
                         :value.sync="searchOptions.last_name"/>
                <n-input label="Имя"
                         :value.sync="searchOptions.first_name"/>
                <n-input label="Отчество"
                         :value.sync="searchOptions.middle_name"/>
                <n-input label="Номер телефона"
                         :value.sync="searchOptions.telephone"/>
            </div>
            <template slot="buttons">
                <n-button
                    @click="createNew"
                    label="Зарегистировать нового"/>
            </template>
        </n-table>
        <doctor-editor :visible.sync="showDialog"
                       :createMode.sync="createMode"
                       @reloadData="reloadData"/>
    </div>
</template>

<script>
import Service from '../service/doctor-service'
import {DOCTORS_TABLE_HEADERS} from "../service/constants";
import DoctorEditor from './dialogs/doctor-editor'

export default {
    name: "doctors",
    components: {DoctorEditor},
    data() {
        return {
            searchOptions: {},
            tableData: [],
            showDialog: false,
            createMode: false,
        }
    },
    methods: {
        loadDoctors() {
            this.$store.commit('SET_PROGRESS', true)
            Service.loadDoctors().then(result => {
                this.$set(this, 'tableData', result.data)
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        reloadData() {
            this.$store.commit('SET_PROGRESS', true)
            Service.loadFilteredDoctors(this.searchOptions).then(result => {
                this.$set(this, 'tableData', result.data)
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        rowClick(item) {
            //todo add controller get doctor by id
            Service.getDoctorById()
            this.$store.commit('SET_SELECTED_DOCTOR', item)
            this.$set(this, 'showDialog', true)
        },
        createNew() {
            //todo remove sync or wtf with row click
            this.$set(this, 'createMode', true)
            this.$set(this, 'showDialog', true)
        }
    },
    computed: {
        columns() {
            return Array.from(DOCTORS_TABLE_HEADERS)
        }
    },
    mounted() {
        this.loadDoctors()
    }
}
</script>

<style scoped>

</style>