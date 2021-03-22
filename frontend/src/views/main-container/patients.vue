<template>
    <div>
        <h3>Список пациентов, зарегистрированных в системе</h3>
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
                    <span class="mr-2">Номер полиса</span>
                    <el-input class="input-width-250" v-model="searchOptions.policy_num"/>
                </div>
            </div>
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
            tableData: [
                {
                    patient_id: 1,
                    first_name: "AAAA",
                    last_name: "BBB",
                    middle_name: "CCC",
                    gender: "м",
                    age: "23",
                    policy_num: "34534534"
                },
                {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 2,
                    first_name: "dffhgfhgf",
                    last_name: "BfghghBB",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                }, {
                    patient_id: 234,
                    first_name: "342432",
                    last_name: "234234",
                    middle_name: "fghhj",
                    gender: "м",
                    age: "23",
                    policy_num: "rt6587"
                },
            ]
        }
    },
    methods: {
        loadPatients() {
            //todo uncomment
            Service.loadPatients()
            //     .then(result => {
            //     this.$set(this, 'tableData', result)
            // })
        },
        rowClick(item) {
            //todo mb get patient by id
            this.$store.commit('SET_SELECTED_PATIENT', item)
            this.goTo('patient')
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