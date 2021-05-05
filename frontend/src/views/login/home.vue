<template>
    <div>
        <main-wrapper :login="true">
            <div class="wrapper-window">
                <div class="login-window">
                    <div class="flr justify-c">
                        <h4 class="ma-3">АВТОРИЗАЦИЯ</h4>
                    </div>
                    <divider/>
                    <div class="pa-5">
                        <transition name="fade">
                            <h4 v-show="errorFlag" class="ma-0 pb-3"
                                style="color: firebrick;">{{ errorMessage }}</h4>
                        </transition>
                        <n-input label="Логин"
                                 :value.sync="user.login"/>
                        <n-input label="Пароль"
                                 @keyup.enter.native.prevent="loginClick"
                                 :password="true"
                                 :value.sync="user.password"/>
                        <n-button
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
import LoginService from '../service/login-service';

export default {
    name: "home",
    data() {
        return {
            user: new User(),
            errorFlag: false
        }
    },
    methods: {
        loginClick() {
            if (this.user.login && this.user.password) {
                LoginService.getUserByLoginPassword(this.user.login, this.user.password).then(result => {
                    if (result.data) {
                        this.$store.commit('SET_AUTH_USER', result.data)
                        this.goTo('home')
                        this.$set(this, 'errorFlag', false)
                    } else {
                        this.$set(this, 'errorFlag', true)
                        setTimeout((scope) => {
                            scope.$set(scope, 'errorFlag', false)
                        }, 3000, this)
                    }
                })
            }
        }
    },
    computed: {
        errorMessage() {
            return 'Неверный логин или пароль!'
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

.fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
}

.fade-enter, .fade-leave-to {
    opacity: 0;
}

</style>