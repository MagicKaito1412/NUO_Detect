<template>
    <div class="fl-сol">
        <div class="fl-row justify-sb">
            <h3>{{ title }}</h3>
            <div class="fl-row" v-if="!creationMode">
                <n-button
                    :disabled="!viewMode"
                    @click="createReport"
                    label="Сформировать отчет"
                />
                <n-button
                    v-if="!fromDoctor"
                    @click="changePass"
                    :full-width="true"
                    label="Сменить пароль"
                />
                <n-button
                    v-if="fromDoctor"
                    :disabled="!viewMode"
                    class="mr-0"
                    @click="goTo('patients')"
                    label="Вернуться к списку пациентов"
                />
            </div>
        </div>
        <divider/>
        <div class="patient">
            <div class="fl-сol width-7">
                <div class="fl-row justify-sb">
                    <h4>Личная информация</h4>
                    <template v-if="fromDoctor">
                        <div class="fl-row" v-if="viewMode">
                            <n-button
                                @click="showLogin"
                                label="Показать логин"
                            />
                            <n-button class="mr-0"
                                      @click="edit"
                                      label="Редактировать"
                            />
                        </div>
                        <div class="fl-row" v-else>
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
                <div class="fl-row justify-sb">
                    <div class="fl-сol">
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
                        <div class="fl-row justify-sb mb-3">
                            <span>Пол</span>
                            <span v-if="viewMode">{{ genderText }}</span>
                            <div class="mr-5" v-else>
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
                    <div class="fl-сol">
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
                    <div class="fl-row justify-sb">
                        <h4>Информация о наличии НУО</h4>
                        <n-button
                            class="mr-0"
                            v-if="fromDoctor && !creationMode"
                            :disabled="!viewMode"
                            @click="predict"
                            :label="predictButton"/>
                    </div>
                    <div class="fl-row justify-sb">
                        <div class="fl-сol">
                            <p class="mb-3">
                                Есть нарушение углеводного обмена:
                            </p>
                        </div>
                        <div class="fl-сol mr-3">
                            <p v-if="viewMode" class="mb-3" style="font-weight: bold">{{ nuoText }}</p>
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
            <div class="fl-сol width-4" v-if="!creationMode">
                <div class="fl-row justify-sb">
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
        <template v-if="showProbs && fromDoctor">
            <div class="fl-row mt-5 mb-5 justify-sb">
                <graph-line
                    v-if="ekgProbsValues"
                    :width="930"
                    :height="300"
                    shape="normal"
                    :axis-min="0"
                    :axis-max="1"
                    :axis-full-mode="true"
                    :labels="ekgLabels"
                    :names="ekgProbsNames"
                    :values="ekgProbsValues">
                    <note text="График вероятностей"></note>
                    <tooltip :names="ekgProbsNames" :position="'right'"></tooltip>
                    <legends :names="ekgProbsNames"></legends>
                    <guideline :tooltip-y="true"></guideline>
                </graph-line>
                <graph-bar
                    v-if="probsValues"
                    :width="500"
                    :height="300"
                    :axis-min="0"
                    :axis-max="1"
                    :bar-margin="10"
                    :bar-padding="5"
                    :labels="ekgProbsNames"
                    :values="probsValues">
                    <note text="Метрики моделей"></note>
                    <tooltip :names="probsNames" :position="'center'"></tooltip>
                    <legends :names="probsNames" :filter="true"></legends>
                </graph-bar>
            </div>
            <n-table :tableData="fullTableData"
                     :columns="fullTableColumns"
                     :showFilters="false"
                     @rowClick="rowClick"/>
        </template>
        <change-pass-dialog :visible.sync="showDialog"/>
        <n-text-dialog :visible.sync="showLoginDialog"
                       :text="loginDialogText"/>
    </div>
</template>

<script>
import PatientService from './patient-service'
import ReportService from '../../service/report-service'
import EkgService from '../ekg/ekg-service'
import ModelTrainService from '../../service/model-train-service'
import {
    EKGS_TABLE_HEADERS,
    POLICY_PATTERN,
    PROBS_EKGS_TABLE_HEADERS,
    TELEPHONE_PATTERN
} from "../../service/constants"
import {Patient} from "../../service/models";
import ChangePassDialog from "../change-pass-dialog";
import UserService from "../../service/user-service";

export default {
    name: "patient",
    components: {ChangePassDialog},
    data() {
        return {
            tableData: [],
            fullTableData: [],
            patient: new Patient(),
            editMode: false,
            creationMode: false,
            radioNuo: '-1',
            radioGender: null, // 1-М, 2-Ж
            showDialog: false,
            showLoginDialog: false,
            newUserLogin: null,
            ekgProbsNames: ['Log Reg', 'Random Forest', 'SVM'],
            probsNames: ['F1', 'Чувствительность', 'Специфичность'],
            ekgLabels: [],
            ekgProbsValues: null,
            probsValues: null,
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
                    this.showLogin()
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
            if (!this.tableData.length) {
                this.showEMessage('Для расчета вероятностей необходимо хотя бы одно измерение ЭКГ')
                return
            }
            this.$store.commit('SET_PROGRESS', true)
            PatientService.predict(this.patient.patient_id).then(result => {
                if (result && result.data === 'OK') {
                    this.$set(this.patient, 'has_probs', true)
                    this.showSMessage('Вероятности успешно расчитаны')
                } else {
                    this.showEMessage('Для расчета вероятностей необходимо обучить модели')
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
        },
        createReport() {
            let patient = {}
            for (const [key, value] of Object.entries(this.patient)) {
                if (!value) continue
                if (key === 'birth_date') {
                    patient[key] = this.formatDate(value)
                } else if (key === 'has_nuo') {
                    patient[key] = this.nuoText
                } else if (key === 'gender') {
                    patient[key] = this.genderText
                } else {
                    patient[key] = `${value}`
                }
            }
            let ekgs = this.fullTableData && this.fullTableData.length
                ? Array.from(this.fullTableData)
                : Array.from(this.tableData)
            let data = {
                patient: patient,
                ekgs: ekgs
            }

            if (this.fromDoctor) { //mb add pictures
                this.$store.commit('SET_PROGRESS', true)
                ReportService.createDocReport(data).then(result => {
                    if (result) {
                        let filename = result.data
                        ReportService.download(filename).then(() => {
                            this.showIMessage('Отчет по пациенту сформирован')
                            ReportService.removeFromFolder(filename)
                        })
                    }
                }).finally(() => {
                    this.$store.commit('SET_PROGRESS', false)
                })
                return
            }
            this.$store.commit('SET_PROGRESS', true)
            ReportService.createPatientReport(data).then(result => {
                if (result) {
                    let filename = result.data
                    ReportService.download(filename).then(() => {
                        this.showIMessage('Отчет сформирован')
                        ReportService.removeFromFolder(filename)
                    })
                }
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        changePass() {
            this.$set(this, 'showDialog', true)
        },
        showLogin() {
            if (!this.patient || !this.patient.user_id) {
                this.showEMessage('Ошибка данных пользователя')
                return
            }
            this.$store.commit('SET_PROGRESS', true)
            UserService.getUserById(this.patient.user_id).then(userResponse => {
                if (userResponse && userResponse.data && userResponse.data.login) {
                    this.$set(this, 'showLoginDialog', true);
                    this.$set(this, 'newUserLogin', userResponse.data.login);
                }
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        fillEkgProbValues(ekgs) {
            let tempLogReg = new Array(ekgs.length)
            let tempRndForest = new Array(ekgs.length)
            let tempSvm = new Array(ekgs.length)
            for (const [idx, item] of ekgs.entries()) {
                this.ekgLabels.push(`${idx + 1}`)
                tempLogReg[idx] = item.prob_log_reg
                tempRndForest[idx] = item.prob_rnd_forest
                tempSvm[idx] = item.prob_log_svm
            }
            this.ekgProbsValues = new Array(3)
            this.ekgProbsValues[0] = tempLogReg
            this.ekgProbsValues[1] = tempRndForest
            this.ekgProbsValues[2] = tempSvm
        },
        fillProbValues() {
            this.$store.commit('SET_PROGRESS', true)
            ModelTrainService.getSensSpec().then(result => {
                if (!result) {
                    return
                }
                if (result && result.data === 'NOT OK') {
                    this.showEMessage('Для расчета метрик моделей необходимо сначала их обучить')
                    return
                }
                if (result && result.data) {
                    let metrics = result.data

                    let tempLogReg = new Array(3)
                    let tempRndForest = new Array(3)
                    let tempSvm = new Array(3)

                    tempLogReg[0] = metrics.logreg_f1
                    tempLogReg[1] = metrics.logreg_sensitivity
                    tempLogReg[2] = metrics.logreg_specificity

                    tempRndForest[0] = metrics.forest_f1
                    tempRndForest[1] = metrics.forest_sensitivity
                    tempRndForest[2] = metrics.forest_specificity

                    tempSvm[0] = metrics.svm_f1
                    tempSvm[1] = metrics.svm_sensitivity
                    tempSvm[2] = metrics.svm_specificity

                    this.$set(this, 'probsValues', [])
                    this.probsValues[0] = tempLogReg
                    this.probsValues[1] = tempRndForest
                    this.probsValues[2] = tempSvm
                }
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
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
            if (this.patient.gender === 2) {
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
        fullTableColumns() {
            let arr = Array.from(EKGS_TABLE_HEADERS)
            arr.push(...Array.from(PROBS_EKGS_TABLE_HEADERS))
            return arr
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
        showProbs() {
            return this.patient.has_probs
        },
        predictButton() {
            return this.showProbs ? 'Обновить расчеты вероятностей' : 'Расчитать вероятность НУО'
        },
        loginDialogText() {
            if (this.newUserLogin) {
                return `Для пользователя зарегистирован логин: ${this.newUserLogin}`
            }
            return ''
        }
    },
    watch: {
        showProbs(val) {
            if (val) {
                this.$store.commit('SET_PROGRESS', true)
                EkgService.loadEkgs(this.patient.patient_id).then(result => {
                    if (result) {
                        this.$set(this, 'fullTableData', result.data)
                        this.fillEkgProbValues(this.fullTableData)
                        this.fillProbValues()
                    }
                }).finally(() => {
                    this.$store.commit('SET_PROGRESS', false)
                })
            }
        }
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