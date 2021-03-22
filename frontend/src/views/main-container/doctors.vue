<template>
    <div>
        <h3>Врачи, зарегистрированные в системе</h3>
        <n-table :tableData="tableData" :columns="columns" @rowClick="rowClick">
            <div class="flr mb-2 justify-sb">
                <div class="flr ">
                    <span class="mr-2">Фамилия</span>
                    <el-input class="input-width-250" v-model="searchOptions.last_name"/>
                </div>
                <div class="flr">
                    <span class="mr-2">Имя</span>
                    <el-input class="input-width-250" v-model="searchOptions.first_name"/>
                </div>
                <div class="flr">
                    <span class="mr-2">Отчество</span>
                    <el-input class="input-width-250" v-model="searchOptions.middle_name"/>
                </div>
                <div class="flr">
                    <span class="mr-2">Номер телефона</span>
                    <el-input class="input-width-250" v-model="searchOptions.telephone"/>
                </div>
            </div>
            <template slot="buttons">
                <el-button @click="createNew">Зарегистировать нового</el-button>
            </template>
        </n-table>
        <doctor-editor :visible.sync="showDialog" :createMode.sync="createMode"/>
    </div>
</template>

<script>
import Service from '../service/service'
import {DOCTORS_TABLE_HEADERS} from "../service/constants";
import DoctorEditor from './dialogs/doctor-editor'

export default {
    name: "doctors",
    components: {DoctorEditor},
    data() {
        return {
            searchOptions: {},
            tableData: [
                {
                    doctor_id: 234,
                    first_name: "Алибек",
                    last_name: "Алибеков",
                    middle_name: "Алибекович",
                    telephone: 4589475845,
                },
            ],
            showDialog: false,
            createMode: false,
        }
    },
    methods: {
        loadDoctors() {
            //todo uncomment
            Service.loadDoctors()
            //     .then(result => {
            //     this.$set(this, 'tableData', result)
            // })
        },
        rowClick(item) {
            //todo mb get patient by id
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