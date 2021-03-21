<template>
    <div>
        <main-wrapper>
            <div class="wrapper-window">
                <div class="login-window">
                    <div class="flr justify-c">
                        <h4 class="ma-3">АВТОРИЗАЦИЯ</h4>
                    </div>
                    <divider/>
                    <div class="pa-2">
                        <div class="mb-2 flr justify-sb">
                            <span class="mr-2">Логин</span>
                            <el-input v-model="user.login"/>
                        </div>
                        <div class="mb-2 flr justify-sb">
                            <span class="mr-2">Пароль</span>
                            <el-input v-model="user.password" show-password/>
                        </div>
                        <div class="primary-button flr justify-c mt-3">
                        <el-button class="width-11">Войти</el-button>
                    </div>
                    </div>
                </div>
            </div>
        </main-wrapper>
    </div>
</template>

<script>
import {User} from "../models";

export default {
    name: "home",
    data() {
    return {
      user: new User()
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
        width: 20%;
        height: fit-content;
        margin-top: 10%;
        border: 1px solid $--color-info-light;
        border-radius: 5px;
        box-shadow: 0 0 10px $--color-info-light;
        position: relative;

    }
}

</style>