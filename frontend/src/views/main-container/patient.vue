<template>
    <div class="flc">
        <h3>{{ title }}</h3>
        <div class="patient">
            <div class="flr">
                <div class="flc">
                    <n-input label="Фамилия"
                             class="mr-5"
                             :readonly="viewMode"
                             :value.sync="patient.last_name"/>
                    <n-input label="Отчество"
                             class="mr-5"
                             :readonly="viewMode"
                             :value.sync="patient.middle_name"/>
                    <n-input label="Пол"
                             class="mr-5"
                             :readonly="viewMode"
                             :value.sync="patient.gender"/>
                    <n-input label="Вес (кг)"
                             class="mr-5"
                             :readonly="viewMode"
                             :value.sync="patient.weight"/>
                    <div class="mt-10">
                        <span v-if="viewMode">
                            Есть нарушение углеводного обмена: {{ patient.has_nuo ? 'ДА' : 'НЕТ' }}</span>
                        <el-checkbox v-if="!viewMode" v-model="patient.has_nuo">
                            Есть нарушение углеводного обмена
                        </el-checkbox>
                    </div>
                    <div class="primary-button mt-3" v-if="viewMode">
                        <el-button class="width-11" @click="edit">Редактировать</el-button>
                    </div>
                    <div class="primary-button mt-3" v-else>
                        <el-button class="width-11" @click="save">Сохранить</el-button>
                    </div>
                </div>
                <div class="flc">
                    <n-input label="Имя"
                             :readonly="viewMode"
                             :value.sync="patient.first_name"/>
                    <n-input label="Номер полиса"
                             :readonly="viewMode"
                             :value.sync="patient.policy_num"/>
                    <n-input label="Возраст"
                             :readonly="viewMode"
                             :value.sync="patient.age"/>
                    <n-input label="Рост (см)"
                             :readonly="viewMode"
                             :value.sync="patient.height"/>
                </div>
            </div>
            <div class="flr" v-if="!creationMode">
                <div class="primary-button">
                    <el-button @click="addEkg">Добавить данные ЭКГ</el-button>
                </div>
                <n-table :tableData="tableData"
                         :columns="columns"
                         :showFilters="false"
                         @rowClick="rowClick"/>
            </div>
        </div>
    </div>
</template>

<script>
import Service from '../service/service'
import {EKGS_TABLE_HEADERS} from "../service/constants";
import {Patient} from "../service/models";

export default {
    name: "patient",
    data() {
        return {
            tableData: [],
            patient: new Patient(),
            editMode: false,
            creationMode: false,
        }
    },
    methods: {
        rowClick(item) {
            //todo get ekg by id
            this.$store.commit('SET_SELECTED_EKG', item)
            this.goTo('ekg')
        },
        loadEkgs() {
            Service.loadEkgs()
        },
        addEkg() {
            Service.addEkg()
        },
        edit() {
            this.$set(this, 'editMode', true);
        },
        save() {
            if (this.creationMode) {
                this.$set(this, 'creationMode', false);
            }
            this.$set(this, 'editMode', false);
            //todo
        }
    },
    computed: {
        getAuthUser() {
            return this.$store.getters.getAuthUser
        },
        //clone obj from store
        getPatient() {
            if (this.getAuthUser.access_level === 2) {
                return this.$store.getters.getSelectedPatient
            }
            return this.$store.getters.getAuthPerson
        },
        title() {
            let editSuffix = this.editMode ? '[Редактирование]' : ''
            let suffix = this.creationMode ? '[Регистрация нового]' : this.editMode ? editSuffix : ''
            return this.getAuthUser.access_level === 2 ? `Данные пациента ${suffix}` : `Карточка пациента ${editSuffix}`
        },
        columns() {
            return Array.from(EKGS_TABLE_HEADERS)
        },
        viewMode() {
            return !this.editMode && !this.creationMode
        }
    },
    mounted() {
        this.loadEkgs()
        this.$set(this, 'creationMode', this.$route.params.creationMode)
    }
}
</script>

<style lang="scss">
.patient {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>