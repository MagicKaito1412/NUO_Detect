<template>
    <div>
        <div class="colored-header">
            <cardio-logo-generator :number="3" v-if="login"/>
            <div class="colored-header __header">
                <img class="main-logo" src="@/assets/search_logo.png"/>
                <h2>Предиктивная система определения наличия НУО</h2>
            </div>
            <cardio-logo-generator :number="login ? 3 : 5"/>
            <div v-if="!login">
                <template v-if="access_level === 2">
                        <el-button class="mr-5 cp" v-if="$route.name !== 'patients'">
                        <i class="material-icons icons-style" @click="goTo('patients')">people</i>
                    </el-button>

                    <el-button class="mr-5 pt-1 cp">
                        <i class="el-icon-set-up icons-style" @click="train"/>
<!--                        TODO decide here-->
<!--                        <i class="material-icons icons-style" @click="train">assessment</i>-->
<!--                        <i class="el-icon-s-operation icons-style" @click="train"/>-->
                    </el-button>
                    <el-button class="mr-5 cp">
                        <i class="material-icons icons-style" @click="doctorCard">account_box</i>
                    </el-button>
                </template>
                <el-button class="mr-5 cp" v-if="access_level === 3 && $route.name !== 'patient'">
                    <i class="material-icons icons-style" @click="goTo('patient')">portrait</i>
                </el-button>
                <el-button class="mr-5 cp">
                    <i class="material-icons icons-style" @click="logout">input</i>
                </el-button>
            </div>
        </div>
        <slot name="default"/>
        <div class="colored-header __footer">
            <h4 class="ma-1">НИУ ВШЭ, 2021</h4>
        </div>
        <n-dialog title="Режим обучения" :visible.sync="showTrainDialog" :hide-back-button="true">
            <span style="white-space: pre-wrap">{{ content }}</span>
            <div class="justify-end" slot="footer">
                <div class="primary-button flr justify-c mt-3">
                    <n-button
                        @click="train"
                        label="Продолжить"
                    />
                    <n-button
                        @click="close"
                        label="Отмена"
                    />
                </div>
            </div>
        </n-dialog>
    </div>
</template>

<script>
export default {
    name: "main-wrapper",
    props: {
        login: {
            type: Boolean,
            default: false
        },
        access_level: {
            type: Number,
            default: 0
        }
    },
    data() {
        return {
            showTrainDialog: false
        }
    },
    methods: {
        train() {
            if (!this.showTrainDialog) {
                this.$set(this, 'showTrainDialog', true)
                return;
            }
            //todo add back + mb preloader
            this.close()
        },
        close() {
            this.$set(this, 'showTrainDialog', false)
        },
        doctorCard() {
            this.goTo('doctor')
        },
        logout() {
            //todo add back
            this.goTo('login')
            this.$store.commit('LOGOUT')
        },
    },
    computed: {
        content() {
            return "Внимание! Вы переходите в режим обучения моделей. В этом режиме будут недоступны основные " +
                "функции системы.\n\nХотите продолжить?"
        }
    }
}
</script>

<style lang="scss">
.colored-header {
    background-color: $--color-primary;
    color: white;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    &.__footer {
        position: absolute;
        justify-content: center;
        bottom: 0;
        width: 100%;
    }

    &.__header {
        justify-content: center;

        .main-logo {
            margin-right: 10px;
            max-width: 50px;
        }
    }

    .cardio-logo {
        max-width: 100px;
    }
}
</style>