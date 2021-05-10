<template>
    <div>
        <main-wrapper :login="true">
            <div class="wrapper-window">
                <div class="login-window">
                    <div class="fl-row justify-c">
                        <h4 class="ma-3">АВТОРИЗАЦИЯ</h4>
                    </div>
                    <divider/>
                    <div class="pa-5">
                        <n-input label="Логин"
                                 :value.sync="user.login"/>
                        <n-input label="Пароль"
                                 @keyup.enter.native.prevent="loginClick"
                                 :password="true"
                                 :value.sync="user.password"/>
                        <n-button
                            class="mr-0"
                            :full-width="true"
                            :disabled="!user.login || !user.password"
                            @click="loginClick"
                            label="Войти"/>
                    </div>
                </div>
            </div>
        </main-wrapper>
    </div>
</template>

<script>
import {User} from "../service/models";
import UserService from '../service/user-service';

export default {
    name: "home",
    data() {
        return {
            user: new User()
        }
    },
    methods: {
        loginClick() {
            if (this.user.login && this.user.password) {
                this.$store.commit('SET_PROGRESS', true)
                UserService.getUserByLoginPassword(this.user.login, this.user.password).then(result => {
                    if (result && result.data) {
                        let authUser = result.data
                        this.$store.commit('SET_AUTH_USER', authUser)
                        UserService.getEntityByUser(authUser).then(entity => {
                            if (entity) {
                                this.$store.commit('SET_AUTH_ENTITY', entity.data)
                                let changePass = false
                                if (this.user.login === this.user.password) {
                                    this.showEMessage('Смените пароль по умолчанию!')
                                    changePass = true
                                }
                                this.goTo('home', {changePass: changePass})
                            }
                        })
                    } else {
                        this.showEMessage('Неверный логин или пароль!')
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
.wrapper-window {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    .login-window {
        width: 25%;
        height: fit-content;
        margin-top: 10%;
        border: 1px solid $--color-info-light;
        border-radius: 5px;
        box-shadow: 0 0 10px $--color-info-light;
        position: relative;
    }
}

</style>