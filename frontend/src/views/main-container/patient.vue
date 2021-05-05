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
                             type="number"
                             :readonly="viewMode"
                             :value.sync="patient.weight"/>
                    <div class="mt-10">
                        <span v-if="viewMode">
                            Есть нарушение углеводного обмена: {{ nuoText }}</span>
                        <n-input v-if="!viewMode" label="Есть нарушение углеводного обмена"
                                 class="mr-5"
                                 :readonly="viewMode"
                                 :value.sync="patient.has_nuo"/>
                    </div>
                    <div class=" mt-3" v-if="viewMode">
                        <n-button
                            @click="edit"
                            label="Редактировать"
                        />
                        <n-button
                            @click="predict"
                            label="Расчитать вероятность НУО"
                        />
                    </div>
                    <div class="flr mt-3" v-else>
                        <n-button
                            @click="save"
                            label="Сохранить"
                        />
                        <n-button
                            @click="cancel"
                            label="Отменить"
                        />
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
                <div class="primary-button ml-5">
                    <n-button
                        @click="addEkg"
                        label="Добавить данные ЭКГ"
                    />
                </div>
                <n-table :tableData="tableData"
                         :columns="columns"
                         :showFilters="false"
                         class="width-8"
                         @rowClick="rowClick"/>
            </div>
        </div>
    </div>
</template>

<script>
import PatientService from '../service/patient-service'
import EkgService from '../service/ekg-service'
import {EKGS_TABLE_HEADERS} from "../service/constants"
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
            EkgService.loadEkgs(this.getPatient.patient_id).then(result => {
                this.$set(this, 'tableData', result.data)
            })
        },
        addEkg() {
            this.goTo('ekg')
        },
        edit() {
            this.$set(this, 'editMode', true);
        },
        save() {
            if (this.creationMode) {
                PatientService.saveNewPatient(this.patient).then(result => {
                    this.$set(this, 'creationMode', false);
                    this.$set(this, 'patient', result.data);
                    this.$store.commit('SET_SELECTED_PATIENT', Object.assign({}, result))
                })
                return
            }
            PatientService.updatePatient(this.patient).then(() => {
                this.$set(this, 'editMode', false)
                this.$store.commit('SET_SELECTED_PATIENT', Object.assign({}, this.patient))
            })
        },
        cancel() {
            if (!this.creationMode) {
                this.$set(this, 'editMode', false)
                this.$set(this, 'patient', Object.assign({}, this.getPatient))
            } else {
                this.goTo('patients')
            }
        },
        predict() {
            //todo
        }
    },
    computed: {
        nuoText() {
            if (this.patient.has_nuo === 1) {
                return 'ДА'
            }
            if (this.patient.has_nuo === 0) {
                return 'НЕТ'
            }
            if (this.patient.has_nuo === -1) {
                return 'НЕИЗВЕСТНО'
            }
            return ''
        },
        getAuthUser() {
            return this.$store.getters.getAuthUser
        },
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
        let routeCreationMode = this.$route.params.creationMode
        this.$set(this, 'creationMode', routeCreationMode ? routeCreationMode : false)
        if (!this.creationMode) {
            this.loadEkgs()
            this.$set(this, 'patient', Object.assign({}, this.getPatient))
        }
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