<template>
    <div class="main-wrapper">
        <div class="colored-header">
            <cardio-logo-generator :number="3" v-if="login"/>
            <div class="colored-header main-header">
                <img class="main-logo" src="@/assets/search_logo.png"/>
                <h2>Предиктивная система определения наличия НУО</h2>
            </div>
            <cardio-logo-generator :number="login ? 3 : 5"/>
            <div v-if="!login" class="fl-row">
                <template v-if="access_level === 2">
                    <el-button :class="`mr-3 cp ${showTrainDialog ? 'active-button': ''}`"
                               @click="train">
                        <span :class="`iconify brain-icon${showTrainDialog ? '-active': ''}`"/>
                    </el-button>

                    <el-button :class="`cp ${route === 'statistics' ? 'active-button': ''}`"
                               @click="goTo('statistics')">
                        <span :class="`iconify statistics-icon${route === 'statistics' ? '-active': ''}`"/>
                    </el-button>

                    <divider type="vertical" style="height: 40px"/>

                    <el-button :class="`mr-3 cp ${route === 'patients' ? 'active-button': ''}`"
                               @click="goTo('patients')">
                        <span :class="`iconify patients-icon${route === 'patients' ? '-active': ''}`"/>
                    </el-button>

                    <el-button :class="`mr-3 cp ${route === 'doctor' ? 'active-button': ''}`"
                               @click="goTo('doctor')">
                        <span :class="`iconify badge-icon${route === 'doctor' ? '-active': ''}`"/>
                    </el-button>
                </template>
                <el-button :class="`mr-3 cp ${route === 'patient' ? 'active-button': ''}`"
                           v-if="access_level === 3"
                           @click="goTo('patient')">
                    <span :class="`iconify patient-icon${route === 'patient' ? '-active': ''}`"/>
                </el-button>
                <el-button class="mr-5 cp" @click="logout">
                    <span class="iconify exit-icon"/>
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
                <div class="primary-button fl-row justify-c mt-3">
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
                ModelTrainService.calcSensSpec()
            }).finally(() => {
                this.$store.commit('SET_PROGRESS', false)
                this.close()
            })
        },
        close() {
            this.$set(this, 'showTrainDialog', false)
        },
        logout() {
            this.goTo('login')
            this.$store.commit('LOGOUT')
        },
    },
    computed: {
        content() {
            return "Внимание! Вы переходите в режим обучения моделей. В этом режиме будут недоступны основные " +
                "функции системы.\n\nХотите продолжить?"
        },
        route() {
            return this.$route.name
        }
    }
}
</script>

<style lang="scss">
body {
    margin: 0;
    overflow-x: hidden;
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
        margin: 0 3px;
        vertical-align: -0.125em;
    }

    .brain-icon {
        content: url('https://api.iconify.design/mdi:brain.svg?color=%235585bf&height=24');

        &-active {
            content: url('https://api.iconify.design/mdi:brain.svg?color=%23295d91&height=24');
        }
        &:hover {
            content: url('https://api.iconify.design/mdi:brain.svg?color=%23295d91&height=24');
        }
    }

    .badge-icon {
        content: url('https://api.iconify.design/mdi:card-account-details.svg?color=%235585bf&height=24');
        //content: url('https://api.iconify.design/mdi:badge-account-horizontal.svg?color=%235585bf&height=24');

        &-active {
            content: url('https://api.iconify.design/mdi:card-account-details.svg?color=%23295d91&height=24');
        }
        &:hover {
            content: url('https://api.iconify.design/mdi:card-account-details.svg?color=%23295d91&height=24');
            //content: url('https://api.iconify.design/mdi:badge-account-horizontal.svg?color=%23295d91&height=24');
        }
    }

    .statistics-icon {
        content: url('https://api.iconify.design/mdi:chart-areaspline.svg?color=%235585bf&height=24');

        &-active {
            content: url('https://api.iconify.design/mdi:chart-areaspline.svg?color=%23295d91&height=24');
        }
        &:hover {
            content: url('https://api.iconify.design/mdi:chart-areaspline.svg?color=%23295d91&height=24');
        }
    }

    .patients-icon {
        content: url('https://api.iconify.design/mdi:account-search.svg?color=%235585bf&height=24');

        &-active {
            content: url('https://api.iconify.design/mdi:account-search.svg?color=%23295d91&height=24');
        }
        &:hover {
            content: url('https://api.iconify.design/mdi:account-search.svg?color=%23295d91&height=24');
        }
    }

    .patient-icon {
        content: url('https://api.iconify.design/mdi:account-details.svg?color=%235585bf&height=24');

        &-active {
            content: url('https://api.iconify.design/mdi:account-details.svg?color=%23295d91&height=24');
        }
        &:hover {
            content: url('https://api.iconify.design/mdi:account-details.svg?color=%23295d91&height=24');
        }
    }

    .exit-icon {
        content: url('https://api.iconify.design/mdi:exit-to-app.svg?color=%235585bf&height=24');

        &:hover {
            content: url('https://api.iconify.design/mdi:exit-to-app.svg?color=%23295d91&height=24');
        }
    }

    .active-button {
        background-color: $--color-primary-light-2;
        cursor: auto;
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