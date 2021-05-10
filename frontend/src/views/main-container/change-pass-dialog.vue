<template>
    <n-dialog :visible="visible"
              title="Смена пароля"
              :showCloseIcon="showCloseIcon"
              @close="close"
              class="change-pass-dialog"
              ref="dialog">
        <div class="fl-сol">
            <n-input
                label="Старый пароль"
                :password="true"
                :value.sync="oldPass"/>
            <n-input
                label="Новый пароль"
                :password="true"
                :value.sync="newPass"/>
            <n-input
                label="Повторите старый пароль"
                @keyup.enter.native.prevent="save"
                :password="true"
                :value.sync="repeatNewPass"/>
            <n-button
                class="mr-0"
                :disabled="disableButton"
                :full-width="true"
                label="Сохранить"
                @click="save"
            />
        </div>
    </n-dialog>
</template>

<script>
import UserService from '../service/user-service'

export default {
    name: "change-pass-dialog",
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        showCloseIcon: {
            type: Boolean,
            default: true
        }
    },
    data() {
        return {
            oldPass: null,
            newPass: null,
            repeatNewPass: null
        }
    },
    computed: {
        disableButton() {
            return !this.oldPass || !this.newPass || !this.repeatNewPass
        }
    },
    methods: {
        save() {
            if (this.disableButton) {
                return
            }
            let authUser = this.$store.getters.getAuthUser
            let user = Object.assign({}, authUser)
            if (this.oldPass !== user.password) {
                this.showWMessage('Старый пароль введен неверно!')
                return
            }
            if (this.oldPass === this.newPass) {
                this.showWMessage('Старый и новый пароли не должны совпадать!')
                return
            }
            if (this.newPass === user.login) {
                this.showWMessage('Логин и пароль не должны совпадать!')
                return
            }
            if (this.newPass !== this.repeatNewPass) {
                this.showWMessage('Новые пароли не совпадают!')
                return
            }
            if (this.newPass.length < 8) {
                this.showWMessage('Длина пароля должна превышать 8 символов')
                return
            }
            user.password = this.newPass
            this.$store.commit('SET_PROGRESS', true)
            UserService.changePassword(user).then(() => {
                this.showSMessage()
                this.$emit('saveButton')
                this.$store.commit('SET_AUTH_USER', user)
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
                this.close()
            })
        },
        close() {
            this.$emit('update:visible', false)
        }
    },
    watch: {
        visible(val) {
            if (val) {
                this.$set(this, 'oldPass', null)
                this.$set(this, 'newPass', null)
                this.$set(this, 'repeatNewPass', null)
            }
        }
    }
}
</script>

<style lang="scss">
.change-pass-dialog {
    .pn-form {
        width: 35%;
    }
}
</style>