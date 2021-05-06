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
                             :value="genderText"
                             v-if="viewMode"/>
                        <div class="flr justify-sb mb-3" v-else>
                            <span>Пол</span>
                            <div class="mr-5">
                                 <el-radio v-model="radioGender"
                                      class="mr-2"
                                      label="1">
                                Мужской
                            </el-radio>
                            <el-radio v-model="radioGender"
                                      label="2">
                                Женский
                            </el-radio>
                            </div>
                        </div>
                    <n-input label="Вес (кг)"
                             class="mr-5"
                             mask="###"
                             :readonly="viewMode"
                             :value.sync="patient.weight"/>
                    <div class="mt-10">
                        <span class="mr-2">
                            Есть нарушение углеводного обмена: {{ viewMode ? nuoText : '' }}
                        </span>
                        <div v-if="!viewMode" class="mr-5 mt-3">
                            <el-radio v-model="radioNuo"
                                      class="mr-2"
                                      label="-1">
                                Не определено
                            </el-radio>
                            <el-radio v-model="radioNuo"
                                      class="mr-2"
                                      label="1">
                                Есть
                            </el-radio>
                            <el-radio v-model="radioNuo"
                                      label="0">
                                Нет
                            </el-radio>
                        </div>
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
                            :disabled="disableSaveButton"
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
                             :placeholder="policyMask"
                             :mask="policyMask"
                             :readonly="viewMode"
                             :value.sync="patient.policy_num"/>
                    <!--todo add field-->
                    <n-date-picker
                        label="Дата рождения"
                    />
                    <n-input label="Возраст"
                             :readonly="viewMode"
                             mask="###"
                             :value.sync="patient.age"/>
                    <n-input label="Рост (см)"
                             :readonly="viewMode"
                             mask="###"
                             :value.sync="patient.height"/>
                </div>
            </div>
            <div class="flr" style="flex-wrap: nowrap;" v-if="!creationMode">
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
import PatientService from '../../service/patient-service'
import EkgService from '../../service/ekg-service'
import {EKGS_TABLE_HEADERS, POLICY_PATTERN} from "../../service/constants"
import {Patient} from "../../service/models";

export default {
    name: "patient",
    data() {
        return {
            tableData: [],
            patient: new Patient(),
            editMode: false,
            creationMode: false,
            radioNuo: '-1',
            radioGender: null, // 1-М, 2-Ж
        }
    },
    methods: {
        rowClick(item) {
            //todo get ekg by id
            this.$store.commit('SET_SELECTED_EKG', item)
            this.goTo('ekg')
        },
        loadEkgs() {
            this.$store.commit('SET_PROGRESS', true)
            EkgService.loadEkgs(this.getPatient.patient_id).then(result => {
                this.$set(this, 'tableData', result.data)
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        addEkg() {
            this.goTo('ekg')
        },
        edit() {
            this.$set(this, 'editMode', true);
        },
        save() {
            this.$set(this.patient, 'has_nuo', Number(this.radioNuo))
            this.$set(this.patient, 'gender', Number(this.radioGender))
            if (this.creationMode) {
                this.$store.commit('SET_PROGRESS', true)
                PatientService.saveNewPatient(this.patient).then(result => {
                    this.$store.commit('SET_PROGRESS', false)
                    this.$set(this, 'creationMode', false);
                    this.$set(this, 'patient', result.data);
                    this.showSMessage()
                    this.$store.commit('SET_SELECTED_PATIENT', Object.assign({}, result))
                })
                return
            }
            this.$store.commit('SET_PROGRESS', true)
            PatientService.updatePatient(this.patient).then(() => {
                this.$store.commit('SET_PROGRESS', false)
                this.$set(this, 'editMode', false)
                this.showSMessage()
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
        genderText() {
            if (this.patient.gender === 1) {
                return 'Мужской'
            }
            if (this.patient.has_nuo === 2) {
                return 'Женский'
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
        },
        policyMask() {
            return POLICY_PATTERN
        },
        disableSaveButton() {
            //todo add required fields
            return false
        }
    },
    mounted() {
        let routeCreationMode = this.$route.params.creationMode
        this.$set(this, 'creationMode', routeCreationMode ? routeCreationMode : false)
        if (!this.creationMode) {
            this.loadEkgs()
            this.$set(this, 'patient', Object.assign({}, this.getPatient))
            this.$set(this, 'radioNuo', `${this.patient.has_nuo}`)
            this.$set(this, 'radioGender', `${this.patient.gender}`)
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