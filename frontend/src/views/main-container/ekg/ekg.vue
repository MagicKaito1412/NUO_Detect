<template>
    <div>
        <div class="flr justify-sb">
            <h3>{{ title }}</h3>
            <div class="flr">
                <template v-if="viewMode">
                    <n-button :label="backButton"
                              @click="goTo('patient', {creationMode: false})"/>
                    <n-button
                        v-if="fromDoctor"
                        @click="edit"
                        label="Редактировать"/>
                </template>
                <template v-else>
                    <n-button
                        @click="save"
                        label="Сохранить"
                    />
                    <n-button
                        @click="cancel"
                        label="Отменить"
                    />
                </template>
            </div>
        </div>
        <div class="flc">
            <n-sub-header label="Общая информация"/>
            <template v-if="viewMode">
                <n-date-picker label="Дата съема ЭКГ"
                               :readonly="true"
                               :value.sync="ekg.registry_date"/>
                <n-time-picker label="Время съема ЭКГ"
                               :readonly="true"
                               :value.sync="ekg.registry_date"/>
            </template>
            <template v-else>
                <n-date-picker label="Дата съема ЭКГ"
                               @keyup.enter.native.prevent="save"
                               :value.sync="registry_date"/>
                <n-time-picker label="Время съема ЭКГ"
                               @keyup.enter.native.prevent="save"
                               :value.sync="registry_time"/>
            </template>
            <n-input label="Частота дыхания (BR)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.br"/>
            <n-input label="Число ударов в секунду"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.pulse"/>
            <n-sub-header label="Подробная информация"/>
            <n-input label="Стандартное отклонение NN-интервалов (SDNN)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.sdnn"/>
            <n-input label="Коэффициент асимметрии NN-интервалов (Skewness)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.skewness"/>
            <n-input label="Амплитуда моды NN-интервалов (AMo)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.amo"/>
            <n-input label="Индекс медленноволновой аритмии (SWAI)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.swai"/>
            <n-input label="Мода NN –интервалов по кардиоинтевалограмме с шагом 100мс (Mo)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.mo"/>
            <n-input label="Вариационный размах RR-интервалов (dRR)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.drr"/>
            <n-input label="Средняя длительность NN-интервалов (RRNN)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.rrnn"/>
            <n-input
                label="Доля пар последовательных NN-интервалов, различающихся более, чем на 50 мс среди всех NN-интервалов (pNN50)"
                @keyup.enter.native.prevent="save"
                :readonly="viewMode"
                :value.sync="ekg.pnn50"/>
            <n-input label="Индекс напряжения (SI)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.si"/>
            <n-input label="Индекс симпато-адреналового тонуса (SATI)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.sati"/>
            <n-input label="Индекс дыхательной модуляции (RMI)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.rmi"/>
            <n-input label="Коэффициент эксцесса NN-интервалов (Kurtosis)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.kurtosis"/>
            <n-input label="Коэффициент вариации NN-интервалов (CV)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.cv"/>
            <n-input label="Среднеквадратичное различие между продолжительностью соседних NN-интервалов (RMSSD)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.rmssd"/>
            <n-input label="Количество пар последовательных NN-интервалов, различающихся более, чем на 50 мс (NN50)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.nn50"/>
            <n-input label="Мощность ВСР в диапазоне низких частот (LF)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.lf"/>
            <n-input
                label="Отношение мощности в диапазоне низких частот к мощности в диапазоне высоких частот (LF/HF)"
                @keyup.enter.native.prevent="save"
                :readonly="viewMode"
                :value.sync="ekg.lfhf"/>
            <n-input label="Отношение мощности в диапазоне высоких частот к общей мощности (HFp=HF/TP)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.hfp"/>
            <n-input label="Мощность ВСР в диапазоне ультранизких частот (ULF)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.ulf"/>
            <n-input label="Общая мощность ВСР (TP=VLF+LF+HF)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.tp"/>
            <n-input label="Мощность ВСР в диапазоне очень низких частот (VLF)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.vlf"/>
            <n-input label="Отношение мощности в диапазоне очень низких частот к общей мощности (VLFp=VLF/TP)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.vlfp"/>
            <n-input label="Отношение мощности в диапазоне низких частот к общей мощности (LFp=LF/TP)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.lfp"/>
            <n-input label="Отношение мощности в диапазоне ультранизких частот к общей мощности (ULFp=ULF/TP)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.ulfp"/>
            <n-input label="Индекс централизации (IC)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.ic"/>
            <n-input label="Мощность ВСР в диапазоне высоких частот (HF)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.hf"/>
            <n-input label="Другая общая мощность ВСР (TPfull=ULF+VLF+LF+HF)"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.tpfull"/>
            <n-input label="Левый склон P-зубца"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.p_left_slopes"/>
            <n-input label="Правый склон P-зубца"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.p_right_slopes"/>
            <n-input label="Левый склон Q-зубца"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.q_left_slopes"/>
            <n-input label="Правый склон Q-зубца"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.q_right_slopes"/>
            <n-input label="Левый склон T-зубца"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.t_left_slopes"/>
            <n-input label="Правый склон T-зубца"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.t_right_slopes"/>
            <n-input label="Ширина интервала QT"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.qt"/>
            <n-input label="Ширина сегмента ST"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.st"/>
            <n-input label="Ширина P-зубца"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.p"/>
            <n-input label="Ширина PQ-интервала"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.pq"/>
            <n-input label="Ширина QRS-комплекса"
                     @keyup.enter.native.prevent="save"
                     :readonly="viewMode"
                     :value.sync="ekg.qrs"/>
            <n-sub-header label="Информация о наличии НУО"/>
            <div class="flr justify-sb">
                <div class="flc">
                    <p class="mb-3">
                        Обнаружено нарушение углеводного обмена:
                    </p>
                    <template v-if="viewMode && fromDoctor">
                        <p class="mb-3">
                            Вероятность НУО по модели логистической регрессии:
                        </p>
                        <p class="mb-3">
                            Вероятность НУО по модели случаного леса:
                        </p>
                        <p class="mb-3">
                            Вероятность НУО по модели SVM:
                        </p>
                    </template>
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
                    <template v-if="viewMode && fromDoctor">
                        <p class="mb-3">{{ prob_log_reg }}</p>
                        <p class="mb-3">{{ prob_rnd_forest }}</p>
                        <p class="mb-3">{{ prob_log_svm }}</p>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {EKG} from "../../service/models";
import EkgService from './ekg-service'
import NTimePicker from "../../../global/components/n-time-picker";

export default {
    name: "ekg",
    components: {NTimePicker},
    data() {
        return {
            ekg: new EKG(),
            creationMode: false,
            editMode: false,
            registry_date: null,
            registry_time: null,
            radioNuo: '-1',
        }
    },
    methods: {
        save() {
            if (!this.validate()) {
                this.showWMessage('Не заполнены обязательные поля!', 'Дата съема ЭКГ, Время съема ЭКГ')
                return
            }
            this.$set(this.ekg, 'has_nuo', Number(this.radioNuo))
            this.$set(this.ekg, 'registry_date', new Date(`${this.registry_date} ${this.registry_time}`))
            if (this.creationMode) {
                this.$store.commit('SET_PROGRESS', true)
                EkgService.saveNewEkg(this.ekg).then(result => {
                    this.$set(this, 'creationMode', false);
                    this.$set(this, 'ekg', result.data);
                    this.showSMessage()
                    this.$store.commit('SET_SELECTED_EKG', Object.assign({}, result.data))
                }).finally(() => {
                    this.$store.commit('SET_PROGRESS', false)
                })
                return
            }
            this.$store.commit('SET_PROGRESS', true)
            EkgService.updateEkg(this.ekg).then(result => {
                this.$set(this, 'editMode', false)
                this.showSMessage()
                this.$store.commit('SET_SELECTED_EKG', Object.assign({}, result.data))
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        edit() {
            this.$set(this, 'editMode', true);
        },
        cancel() {
            if (!this.creationMode) {
                this.$set(this, 'editMode', false)
                this.$set(this, 'ekg', Object.assign({}, this.getEkg))
                this.$set(this, 'registry_date', this.ekg.registry_date)
                this.$set(this, 'registry_time', this.ekg.registry_date)
            } else {
                this.goTo('patient')
            }
        },
        validate() {
            return this.registry_date && this.registry_time
        }
    },
    computed: {
        getEkg() {
            return this.$store.getters.getSelectedEkg
        },
        title() {
            let editSuffix = this.editMode ? '[Редактирование]' : ''
            let suffix = this.creationMode ? '[Регистрация нового]' : this.editMode ? editSuffix : ''
            return `ЭКГ пациента ${suffix}`
        },
        viewMode() {
            return !this.editMode && !this.creationMode
        },
        nuoText() {
            if (this.ekg.has_nuo === 1) {
                return 'ДА'
            }
            if (this.ekg.has_nuo === 0) {
                return 'НЕТ'
            }
            if (this.ekg.has_nuo === -1) {
                return 'НЕИЗВЕСТНО'
            }
            return ''
        },
        prob_log_reg() {
            return this.ekg.prob_log_reg === -1 ? 'Не определена' : this.ekg.prob_log_reg
        },
        prob_rnd_forest() {
            return this.ekg.prob_rnd_forest === -1 ? 'Не определена' : this.ekg.prob_rnd_forest
        },
        prob_log_svm() {
            return this.ekg.prob_log_svm === -1 ? 'Не определена' : this.ekg.prob_log_svm
        },
        fromDoctor() {
            let getAuthUser = this.$store.getters.getAuthUser
            return getAuthUser && getAuthUser.access_level === 2
        },
        backButton() {
            return this.fromDoctor ? 'К карточке пациента' : 'К личным данным'
        }
    },
    mounted() {
        let routeCreationMode = this.$route.params.creationMode
        this.$set(this, 'creationMode', routeCreationMode ? routeCreationMode : false)
        if (!this.creationMode) {
            this.$set(this, 'ekg', Object.assign({}, this.getEkg))
            this.$set(this, 'radioNuo', `${this.ekg.has_nuo}`)
            this.$set(this, 'registry_date', this.ekg.registry_date)
            this.$set(this, 'registry_time', this.ekg.registry_date)
        }
    }
}
</script>

<style scoped>

</style>