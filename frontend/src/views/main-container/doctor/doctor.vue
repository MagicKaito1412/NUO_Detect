<template>
    <div class="fl-row">
        <img class="avatar" src="@/assets/doc.png"/>
        <div class="fl-сol justify-sb" style="margin-right: 150px;">
            <h3 class="mt-0 mb-7">Личная информация</h3>
            <n-input
                :value.sync="doctor.last_name"
                :readonly="!editMode"
                @keyup.enter.native.prevent="save"
                label="Фамилия"
            />
            <n-input
                :value.sync="doctor.first_name"
                :readonly="!editMode"
                @keyup.enter.native.prevent="save"
                label="Имя"
            />
            <n-input
                :value.sync="doctor.middle_name"
                :readonly="!editMode"
                @keyup.enter.native.prevent="save"
                label="Отчество"
            />
            <n-input
                :maxlength="6"
                :value.sync="doctor.cabinet"
                :readonly="!editMode"
                @keyup.enter.native.prevent="save"
                label="Кабинет"
            />
            <n-input
                :value.sync="doctor.telephone"
                :readonly="!editMode"
                @keyup.enter.native.prevent="save"
                :placeholder="telephoneMask"
                :mask="telephoneMask"
                label="Телефон"
            />
            <n-input
                :value.sync="doctor.email"
                :readonly="!editMode"
                @keyup.enter.native.prevent="save"
                label="E-mail"
            />
        </div>
        <div class="fl-сol width-2">
            <template v-if="!editMode">
                <n-button
                    @click="edit"
                    :full-width="true"
                    label="Редактировать личные данные"
                />
                <n-button
                    @click="changePass"
                    :full-width="true"
                    label="Сменить пароль"
                />
            </template>
            <template v-else>
                <n-button
                    @click="save"
                    :full-width="true"
                    label="Сохранить"
                />
                <n-button
                    @click="cancel"
                    :full-width="true"
                    label="Отменить"
                />
            </template>
        </div>
        <change-pass-dialog :visible.sync="showDialog"/>
    </div>
</template>

<script>
import {Doctor} from "../../service/models";
import {TELEPHONE_PATTERN} from "../../service/constants";
import DoctorService from "./doctor-service";
import ChangePassDialog from "../change-pass-dialog";

export default {
    name: "doctor",
    components: {ChangePassDialog},
    data() {
        return {
            doctor: new Doctor(),
            editMode: false,
            showDialog: false
        }
    },
    methods: {
        save() {
            this.$store.commit('SET_PROGRESS', true)
            DoctorService.updateDoctor(this.doctor).then(() => {
                this.showSMessage()
                this.$set(this, 'editMode', false)
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
            })
        },
        edit() {
            this.$set(this, 'editMode', true)
        },
        cancel() {
            this.$set(this, 'editMode', false)
            this.$set(this, 'doctor', Object.assign({}, this.authEntity))
        },
        changePass() {
            this.$set(this, 'showDialog', true)
        }
    },
    computed: {
        telephoneMask() {
            return TELEPHONE_PATTERN
        },
        authEntity() {
            return this.$store.getters.getAuthEntity
        },
    },
    mounted() {
        let authEntity = this.$store.getters.getAuthEntity
        this.$set(this, 'doctor', Object.assign({}, authEntity))
    }
}
</script>

<style lang="scss">
.avatar {
    max-width: 200px;
    margin-right: 150px;
}
</style>