<template>
    <n-dialog :visible="visible" :title="title" @close="close">
        <div class="flr justify-sb">
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
                :maxlength="11"
                :value.sync="doctor.telephone"
                @keyup.enter.native.prevent="save"
                label="Телефон"
            />
            <n-input
                :value.sync="doctor.email"
                @keyup.enter.native.prevent="save"
                label="E-mail"
            />
        </div>
        <div class="primary-button flr justify-c mt-3">
            <n-button
                @click="save"
                label="Сохранить"/>
        </div>
    </n-dialog>
</template>

<script>
import {Doctor} from "../../service/models";
import Service from '../../service/doctor-service'

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
            if (this.createMode) {
                return `Регистрация нового пользователя`
            }
            let middleName = this.getSelectedDoctor.middle_name ? this.getSelectedDoctor.middle_name : ''
            let fullName = `${this.getSelectedDoctor.last_name} ${this.getSelectedDoctor.first_name}
            ${middleName} (${this.getSelectedDoctor.doctor_id})`
            return `Редактирование пользователя ${fullName}`
        }
    },
    methods: {
        close() {
            this.$emit('update:createMode', false)
            this.$emit('update:visible', false)
            this.$emit('reloadData')
        },
        save() {
            if (this.createMode) {
                Service.saveNewDoctor(this.doctor).then(result => {
                    this.$set(this, 'doctor', result.data);
                }).finally(() => {
                    this.close()
                })
            } else {
                //todo
                Service.updateDoctor()
            }
        },
        initEditFields() {
            this.$nextTick(() => {
                for (const [key, value] of Object.entries(this.getSelectedDoctor)) {
                    this.$set(this.doctor, `${key}`, value)
                }
            })
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

<style scoped>

</style>