<template>
    <n-dialog :visible="visible" :title="title" @close="close">
        <div class="flr justify-sb">
            <n-input
                :spaceBetween="false"
                :value.sync="doctor.last_name"
                label="Фамилия"
            />
            <n-input
                :spaceBetween="false"
                :value.sync="doctor.first_name"
                label="Имя"
            />
        </div>
        <n-input
            :spaceBetween="false"
            :value.sync="doctor.middle_name"
            label="Отчество"
        />
        <div class="flr justify-sb">
            <n-input
                :spaceBetween="false"
                type="number"
                :maxlength="11"
                :value.sync="doctor.telephone"
                label="Телефон"
            />
            <n-input
                :spaceBetween="false"
                :value.sync="doctor.telephone"
                label="Кабинет"
            />
        </div>
        <div class="primary-button flr justify-c mt-3">
            <el-button class="width-11" @click="save">Сохранить</el-button>
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
        },
        save() {
            //todo
            if (this.createMode) {
                Service.saveNewDoctor()
            } else {
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