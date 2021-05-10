<template>
    <transition name="modal" v-if="visible">
        <div class="modal-mask">
            <div class="modal-wrapper">
                <div class="modal-container modal-dialog" :class="sizeClass">
                    <div class="pn-form">
                        <div class="pn-form-heading">
                            <div class="pn-form-heading__inner fl-row justify-c align-c">
                                <h3>{{ title }}</h3>
                                <i class="material-icons close-icon"
                                   @click="close"
                                   v-if="showCloseIcon">close</i>
                            </div>
                            <divider v-if="showDivider"/>
                        </div>
                        <div class="pn-form-inner">
                            <slot name="default"/>
                            <slot name="footer"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
import {disableBodyScroll, clearAllBodyScrollLocks} from 'body-scroll-lock'

export default {
    name: "n-dialog",
    props: {
        title: {
            type: String,
            default: null
        },
        size: {
            type: Number,
            default: null
        },
        visible: {
            type: Boolean,
            default: false
        },
        showCloseIcon: {
            type: Boolean,
            default: true
        },
        showDivider: {
            type: Boolean,
            default: true
        },
    },
    methods: {
        close() {
            this.$emit('close')
            this.$emit('update:visible', false)
        },
    },

    computed: {
        sizeClass() {
            return 'modal-' + (this.size || 'md')
        }

    },

    watch: {
        visible(val) {
            if (val) {
                disableBodyScroll(this.$el)
            } else {
                clearAllBodyScrollLocks()
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.pn-form {
    background-color: white;
    box-shadow: 0 6px 12px 0 rgba(0, 0, 0, 0.05);
    margin: 0 auto;
    width: 50%;
}

.pn-form-heading {
    font-size: 15px;
    font-weight: 500;
    text-align: center;
    color: black;
    box-shadow: 0 1px 0 0 white;
}

.pn-form-heading__inner {
    position: relative;
    padding-right: 40px;
    padding-left: 15px;

    .close-icon {
        position: absolute;
        right: 0;
        padding-right: 15px;
        cursor: pointer;
        color: $--color-primary;
        &:hover {
            color: $--color-primary-dark;
        }
    }
}

.pn-form-heading__title {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    height: 7px;
    width: 13px;
    margin-top: -4px;
    font-size: 5.6px;
    color: $--color-info;
}

.pn-form-heading__close {
    position: absolute;
    right: 20px;
    top: 50%;
    margin-top: -5px;
    width: 12px;
    height: 12px;
    background: white;
    background-size: cover;
    cursor: pointer;
}

.pn-iconfont-up {
    cursor: pointer;
}

.pn-form-inner {
    padding: 20px;
    display: flex;
    flex-direction: column;
}

/* Фон при открытом модальном окне */
.modal-mask {
    position: fixed;
    z-index: 2000;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: table;
    transition: opacity 0.3s ease;
}

.modal-wrapper {
    display: table-cell;
    vertical-align: middle;
}

.modal-container {
    margin: 0 auto;
    transition: all 0.3s ease;
}

.modal-body {
    max-height: 600px;
    overflow-y: scroll; /* has to be scroll, not auto */
    -webkit-overflow-scrolling: touch;
}

.modal-enter {
    opacity: 0;
}

.modal-leave-active {
    opacity: 0;
}

.modal-enter .modal-container {
    transform: scale(1.1);
}

.modal-leave-active .modal-container {
    transform: scale(1.1);
}
</style>
