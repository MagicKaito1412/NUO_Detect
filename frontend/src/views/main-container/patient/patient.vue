<template>
    <div class="flc">
        <div class="flr justify-sb">
            <h3>{{ title }}</h3>
            <div class="flr" v-if="fromDoctor">
                <template v-if="viewMode">
                    <n-button
                        @click="edit"
                        label="Редактировать личные данные"
                    />
                </template>
                <template v-else>
                    <n-button
                        :disabled="disableSaveButton"
                        @click="save"
                        label="Сохранить"
                    />
                    <n-button
                        @click="cancel"
                        label="Отменить"
                    />
                </template>
                <n-button
                    class="mr-0"
                    :disabled="!viewMode"
                    @click="addEkg"
                    label="Добавить данные ЭКГ"
                />
            </div>
        </div>
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
                        <n-button
                            v-if="fromDoctor"
                            :disabled="!viewMode"
                            @click="predict"
                            label="Расчитать вероятность НУО"
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
                        :readonly="viewMode"
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
            <n-table :tableData="tableData"
                     :columns="columns"
                     :showFilters="false"
                     class="width-4"
                     @rowClick="rowClick"
                     v-if="!creationMode"/>
        </div>
    </div>
</template>

<script>
import PatientService from '../../service/patient-service'
import EkgService from '../../service/ekg-service'
import {EKGS_TABLE_HEADERS, POLICY_PATTERN} from "../../service/constants"
import {Patient} from "../../service/models";
import LoginService from "../../service/login-service";

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
            }).finally(() => {
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
                    this.$set(this, 'creationMode', false);
                    this.$set(this, 'patient', result.data);
                    this.showSMessage()
                    this.$store.commit('SET_SELECTED_PATIENT', Object.assign({}, result))
                }).finally(() => {
                    this.$store.commit('SET_PROGRESS', false)
                })
                return
            }
            this.$store.commit('SET_PROGRESS', true)
            PatientService.updatePatient(this.patient).then(() => {
                this.$set(this, 'editMode', false)
                this.showSMessage()
                this.$store.commit('SET_SELECTED_PATIENT', Object.assign({}, this.patient))
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
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
            return this.getAuthUser.access_level === 2 ? `Данные пациента ${suffix}` : `Личные данные ${editSuffix}`
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
        fromDoctor() {
            return this.$route.params.fromDoctor
        },
        disableSaveButton() {
            //todo add required fields
            return false
        }
    },
    mounted() {
        if (this.fromDoctor) {
            let routeCreationMode = this.$route.params.creationMode
            this.$set(this, 'creationMode', routeCreationMode ? routeCreationMode : false)
            if (!this.creationMode) {
                this.loadEkgs()
                this.$set(this, 'patient', Object.assign({}, this.getPatient))
                this.$set(this, 'radioNuo', `${this.patient.has_nuo}`)
                this.$set(this, 'radioGender', `${this.patient.gender}`)
            }
        } else {
            if (!this.authEntity || !this.authEntity.user_id) {
                let authUser = this.$store.getters.getAuthUser
                this.$store.commit('SET_PROGRESS', true)
                LoginService.getEntityByUser(authUser).then(result => {
                    if (result) {
                        this.$set(this, 'patient', result.data)
                        this.$store.commit('SET_AUTH_ENTITY', Object.assign({}, this.patient))
                    }
                }).finally(() => {
                    this.$store.commit('SET_PROGRESS', false)
                })
            }
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