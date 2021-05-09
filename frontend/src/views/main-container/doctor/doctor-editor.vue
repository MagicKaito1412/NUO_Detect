<template>
    <n-dialog :visible="visible" :title="title" @close="close" class="doctor-editor">
        <div class="fl-сol justify-sb">
            <n-input
                :value.sync="doctor.last_name"
                @keyup.enter.native.prevent="save"
                label="Фамилия"
            />
            <n-input
                :value.sync="doctor.first_name"
                @keyup.enter.native.prevent="save"
                label="Имя"
            />
            <n-input
                :value.sync="doctor.middle_name"
                @keyup.enter.native.prevent="save"
                label="Отчество"
            />
            <n-input
                :maxlength="6"
                :value.sync="doctor.cabinet"
                @keyup.enter.native.prevent="save"
                label="Кабинет"
            />
            <n-input
                :value.sync="doctor.telephone"
                @keyup.enter.native.prevent="save"
                :placeholder="telephoneMask"
                :mask="telephoneMask"
                label="Телефон"
            />
            <n-input
                :value.sync="doctor.email"
                @keyup.enter.native.prevent="save"
                label="E-mail"
            />
        </div>
        <div class="primary-button fl-row justify-c mt-3">
            <n-button
                @click="save"
                label="Сохранить"/>
            <n-button
                v-if="!createMode"
                @click="remove"
                type="error"
                label="Удалить"/>
        </div>
    </n-dialog>
</template>

<script>
import {Doctor} from "../../service/models";
import DoctorService from './doctor-service'
import {TELEPHONE_PATTERN} from "../../service/constants";

export default {
    name: "doctor-editor",
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        createMode: {
            type: Boolean,
            default: false
        },
    },
    data() {
        return {
            doctor: new Doctor()
        }
    },
    computed: {
        getSelectedDoctor() {
            return this.$store.getters.getSelectedDoctor
        },
        title() {
            return this.createMode ? `Регистрация нового пользователя` : `Редактирование пользователя`
        },
        telephoneMask() {
            return TELEPHONE_PATTERN
        }
    },
    methods: {
        close() {
            this.$emit('update:createMode', false)
            this.$emit('update:visible', false)
            this.$emit('reloadData')
            this.$store.commit('SET_PROGRESS', false)
        },
        save() {
            if (!this.validate()) {
                this.showWMessage('Не заполнены обязательные поля!', 'Фамилия, Имя, Телефон')
                return
            }
            if (this.createMode) {
                this.$store.commit('SET_PROGRESS', true)
                DoctorService.saveNewDoctor(this.doctor).then(() => {
                    this.showSMessage()
                }).finally(() => {
                    this.close()
                })
            } else {
                this.$store.commit('SET_PROGRESS', true)
                DoctorService.updateDoctor(this.doctor).then(() => {
                    this.showSMessage()
                }).finally(() => {
                    this.close()
                })
            }
        },
        remove() {
            this.$store.commit('SET_PROGRESS', true)
            DoctorService.deleteDoctor(this.doctor.doctor_id).then(() => {
                this.showSMessage('Информация о враче удалена из базы')
            }).finally(() => {
                this.close()
            })
        },
        initEditFields() {
            this.$nextTick(() => {
                for (const [key, value] of Object.entries(this.getSelectedDoctor)) {
                    this.$set(this.doctor, `${key}`, value)
                }
            })
        },
        validate() {
            return this.doctor.first_name
                && this.doctor.last_name
                && this.doctor.telephone
        }
    },
    watch: {
        visible(val) {
            if (val) {
                if (!this.createMode && this.getSelectedDoctor) {
                    this.initEditFields()
                }
            } else {
                this.$set(this, 'doctor', new Doctor())
            }
        }
    }
}
</script>

<style lang="scss">
.doctor-editor {
    .pn-form {
        width: 30%;
    }
}
</style>