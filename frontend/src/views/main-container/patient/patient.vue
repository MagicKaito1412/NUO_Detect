<template>
    <div class="flc">
        <div class="flr justify-sb">
            <h3>{{ title }}</h3>
            <div class="flr" v-if="fromDoctor && !creationMode">
                <n-button
                    :disabled="!viewMode"
                    class="mr-0"
                    @click="goTo('patients')"
                    label="Вернуться к списку пациентов"
                />
                <!--                todo remove later-->
                <!--                <template v-if="viewMode">-->
                <!--                    <n-button-->
                <!--                        @click="edit"-->
                <!--                        label="Редактировать личные данные"-->
                <!--                    />-->
                <!--                </template>-->
                <!--                <template v-else-if="!creationMode">-->
                <!--                    <n-button-->
                <!--                        @click="save"-->
                <!--                        label="Сохранить"-->
                <!--                    />-->
                <!--                    <n-button-->
                <!--                        @click="cancel"-->
                <!--                        label="Отменить"-->
                <!--                    />-->
                <!--                </template>-->
                <!--                <n-button-->
                <!--                    class="mr-0"-->
                <!--                    :disabled="!viewMode"-->
                <!--                    @click="addEkg"-->
                <!--                    label="Добавить данные ЭКГ"-->
                <!--                    v-if="!creationMode"-->
                <!--                />-->
            </div>
        </div>
        <divider/>
        <div class="patient">
            <div class="flc width-7">
                <div class="flr justify-sb">
                    <h4>Личная информация</h4>
                    <template v-if="fromDoctor">
                        <n-button class="mr-0"
                                  @click="edit"
                                  v-if="viewMode"
                                  label="Редактировать"
                        />
                        <div class="flr" v-else>
                            <n-button
                                @click="save"
                                label="Сохранить"
                            />
                            <n-button
                                class="mr-0"
                                @click="cancel"
                                label="Отменить"
                            />
                        </div>
                    </template>
                </div>
                <div class="flr justify-sb">
                    <div class="flc">
                        <n-input label="Фамилия"
                                 @keyup.enter.native.prevent="save"
                                 :readonly="viewMode"
                                 :value.sync="patient.last_name"/>
                        <n-input label="Имя"
                                 @keyup.enter.native.prevent="save"
                                 :readonly="viewMode"
                                 :value.sync="patient.first_name"/>
                        <n-input label="Отчество"
                                 @keyup.enter.native.prevent="save"
                                 :readonly="viewMode"
                                 :value.sync="patient.middle_name"/>
                        <n-input label="Пол"
                                 @keyup.enter.native.prevent="save"
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
                        <!-- todo remove age required prop-->
                        <n-date-picker
                            label="Дата рождения"
                            :placeholder="viewMode ? '' : 'дд.мм.гггг'"
                            :readonly="viewMode"
                            :value.sync="patient.birth_date"
                            @keyup.enter.native.prevent="save"/>
                        <n-input label="Возраст"
                                 :readonly="viewMode"
                                 @keyup.enter.native.prevent="save"
                                 mask="###"
                                 :value.sync="patient.age"/>
                    </div>
                    <div class="flc">
                        <n-input label="Вес (кг)"
                                 mask="###"
                                 @keyup.enter.native.prevent="save"
                                 :readonly="viewMode"
                                 :value.sync="patient.weight"/>
                        <n-input label="Рост (см)"
                                 :readonly="viewMode"
                                 @keyup.enter.native.prevent="save"
                                 mask="###"
                                 :value.sync="patient.height"/>
                        <n-input label="Номер полиса"
                                 @keyup.enter.native.prevent="save"
                                 :placeholder="viewMode ? '' : policyMask"
                                 :mask="policyMask"
                                 :readonly="viewMode"
                                 :value.sync="patient.policy_num"/>
                        <n-input
                            :value.sync="patient.telephone"
                            :readonly="viewMode"
                            @keyup.enter.native.prevent="save"
                            :placeholder="viewMode ? '' : telephoneMask"
                            :mask="telephoneMask"
                            label="Телефон"
                        />
                        <n-input
                            :value.sync="patient.email"
                            :readonly="viewMode"
                            @keyup.enter.native.prevent="save"
                            label="E-mail"
                        />
                    </div>
                </div>
                <div class="mt-10">
                    <divider/>
                    <div class="flr justify-sb">
                        <h4>Информация о наличии НУО</h4>
                        <n-button
                            class="mr-0"
                            v-if="fromDoctor && !creationMode"
                            :disabled="!viewMode"
                            @click="predict"
                            label="Расчитать вероятность НУО"/>
                    </div>
                    <div class="flr justify-sb">
                        <div class="flc">
                            <p class="mb-3">
                                Есть нарушение углеводного обмена:
                            </p>
                        </div>
                        <div class="flc mr-3">
                            <p v-if="viewMode" class="mb-3">{{ nuoText }}</p>
                            <div v-else class="mr-5 mt-3">
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
                    </div>
                </div>
            </div>
            <div class="flc width-4" v-if="!creationMode">
                <div class="flr justify-sb">
                    <h4>Информация по ЭКГ</h4>
                    <n-button
                        class="mr-0"
                        :disabled="!viewMode"
                        @click="addEkg"
                        label="Добавить данные ЭКГ"
                        v-if="fromDoctor"
                    />
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
import PatientService from './patient-service'
import EkgService from '../ekg/ekg-service'
import {EKGS_TABLE_HEADERS, POLICY_PATTERN, TELEPHONE_PATTERN} from "../../service/constants"
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
            showProbs: false //todo
        }
    },
    methods: {
        rowClick(item) {
            if (!this.editMode) {
                EkgService.getEkgById(item.ekg_id).then(result => {
                    if (result) {
                        this.$store.commit('SET_SELECTED_EKG', result.data)
                        this.goTo('ekg')
                    }
                })
            }
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
            this.goTo('ekg', {creationMode: true})
        },
        edit() {
            this.$set(this, 'editMode', true);
        },
        save() {
            this.$set(this.patient, 'has_nuo', Number(this.radioNuo))
            this.$set(this.patient, 'gender', Number(this.radioGender))
            if (!this.validate()) {
                this.showWMessage('Не заполнены обязательные поля!',
                    'Фамилия, Имя, Пол, Возраст, Рост, Вес, Номер полиса') //todo change
                return
            }
            this.$set(this.patient, 'birth_date', new Date(`${this.patient.birth_date}`))
            if (this.creationMode) {
                this.$store.commit('SET_PROGRESS', true)
                PatientService.saveNewPatient(this.patient).then(result => {
                    this.$set(this, 'creationMode', false);
                    this.$set(this, 'patient', result.data);
                    this.showSMessage()
                    this.$store.commit('SET_SELECTED_PATIENT', Object.assign({}, result.data))
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
            this.$store.commit('SET_PROGRESS', true)
            PatientService.predict(this.patient.patient_id).then(result => {
                if (result) {
                    this.$set(this, 'showProbs', true)
                    this.showSMessage('Вероятности успешно расчитаны')
                }
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        validate() {
            return this.patient.first_name
                && this.patient.last_name
                && this.patient.gender
                && this.patient.age //todo change on birth_date after back
                && this.patient.weight
                && this.patient.height
                && this.patient.policy_num
        },
        loadPatient() {
            this.$set(this, 'creationMode', false)
            this.loadEkgs()
            this.$set(this, 'patient', Object.assign({}, this.getPatient))
            this.$set(this, 'radioNuo', `${this.patient.has_nuo}`)
            this.$set(this, 'radioGender', `${this.patient.gender}`)
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
            return this.$store.getters.getAuthEntity
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
            return this.getAuthUser && this.getAuthUser.access_level === 2
        },
        telephoneMask() {
            return TELEPHONE_PATTERN
        },
    },
    mounted() {
        if (this.fromDoctor) { //from doctor account
            let routeCreationMode = this.$route.params.creationMode
            this.$set(this, 'creationMode', routeCreationMode ? routeCreationMode : false)
            if (!this.creationMode) {
                this.loadPatient()
            }
        } else { //from patient account
            this.loadPatient()
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