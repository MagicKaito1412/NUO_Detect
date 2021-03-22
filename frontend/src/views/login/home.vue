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
                        <div class="mb-2 flr justify-sb">
                            <span class="mr-2">Логин</span>
                            <el-input class="input-width-250" v-model="user.login"/>
                        </div>
                        <div class="mb-2 flr justify-sb">
                            <span class="mr-2">Пароль</span>
                            <el-input class="input-width-250" v-model="user.password" show-password/>
                        </div>
                        <div class="primary-button flr justify-c mt-3">
                            <el-button style="width: 100%; margin: 7px 0 0 0; padding: 5px 0;" @click="loginClick">Войти</el-button>
                        </div>
                    </div>
                </div>
            </div>
        </main-wrapper>
    </div>
</template>

<script>
import {User} from "../service/models";

export default {
    name: "home",
    data() {
        return {
            user: new User()
        }
    },
    methods: {
        loginClick() {
            //todo add back
            this.$set(this.user, 'id', 1)
            this.$set(this.user, 'access_level', Number(this.user.login))
            this.$store.commit('SET_AUTH_USER', this.user)
            this.goTo('home')
        }
    }
}
</script>

<style lang="scss">
.wrapper-window {
    display: flex;
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