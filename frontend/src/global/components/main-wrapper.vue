<template>
    <div class="main-wrapper">
        <div class="colored-header">
            <cardio-logo-generator :number="3" v-if="login"/>
            <div class="colored-header main-header">
                <img class="main-logo" src="@/assets/search_logo.png"/>
                <h2>Предиктивная система определения наличия НУО</h2>
            </div>
            <cardio-logo-generator :number="login ? 3 : 5"/>
            <div v-if="!login" class="flr">
                <template v-if="access_level === 2">
                    <el-button class="pt-1 cp" @click="train">
<!--                        <i class="material-icons icons-style" @click="train">memory</i>-->
                        <span class="iconify" data-icon="mdi:brain" data-inline="false"></span>
                    </el-button>
                    <divider type="vertical" style="height: 40px"/>
                    <el-button class="mr-5 cp" v-if="$route.name !== 'patients'">
                        <i class="material-icons icons-style" @click="goTo('patients')">people</i>
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
        <div class="wrapper__body">
            <slot name="default"/>
        </div>
        <div class="colored-header main-footer">
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
import ModelTrainService from '../../views/service/model-train-service'

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
            this.$store.commit('SET_PROGRESS', true)
            ModelTrainService.train().then(() => {
                this.showSMessage('Обучение моделей успешно завершено')
                //todo this.goTo('training-results')
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
                this.close()
            })
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
body {
   margin: 0;
}
.main-wrapper {
    display: flex;
    flex-flow: column nowrap;
    width: 100vw;
    height: 100vh;

    .main-header {
        justify-content: center;
        flex: 0 0 auto;

        .main-logo {
            margin-right: 10px;
            max-width: 50px;
        }
    }

    .wrapper__body {
        flex: 1 1 auto;
        align-items: center;
        justify-content: center;
    }

    .main-footer {
        flex: 0 0 auto;
        justify-content: center;
    }

    .iconify {
        margin: 0 2px;
        content: url('https://api.iconify.design/mdi:brain.svg?color=%235585bf&height=24');
        vertical-align: -0.125em;
        &:hover {
            //content: url('https://api.iconify.design/mdi:brain.svg?color=%233c8aa9&height=24');
            content: url('https://api.iconify.design/mdi:brain.svg?color=%23295d91&height=24');
        }
    }
}


.colored-header {
    background-color: $--color-primary;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .cardio-logo {
        max-width: 100px;
    }
}
</style>