<template>
    <div class="n-button">
        <el-button :class="classes"
                   :style="fullWidth ? 'width: 100%;' : ''"
                   :disabled="disabled"
                   @click="$emit('click')">
            {{ label }}
        </el-button>
    </div>
</template>

<script>
export default {
    name: "n-button",
    props: {
        disabled: {
            type: Boolean,
            default: false
        },
        fullWidth: {
            type: Boolean,
            default: false
        },
        type: {
            type: String,
            default: 'primary' //primary, default
        },
        label: {
            type: String,
            default: ''
        },
        customClass: {
            type: String,
            default: null
        }
    },
    computed: {
        classes() {
            return {
                ['disabled-button']: this.disabled,
                ['primary-button']: this.type === 'primary',
                [`${this.customClass}`]: this.customClass
            }
        }
    }
}
</script>

<style lang="scss">
.n-button {
    margin-top: 12px;
    span {
      font-size: 14px;
    }

    .primary-button {
        background-color: $--color-primary;
        color: white;
        border: 1px solid $--color-primary;

        &:hover {
            background-color: $--color-primary-light;
        }
    }

    .disabled-button {
        background-color: $--color-primary-lighter;
        color: $--color-info-lighter;
        border: 1px solid $--color-info;
        cursor: not-allowed !important;

        &:hover {
            background-color: $--color-primary-lighter;
        }
    }

    .el-button {
        cursor: pointer;
        padding: 10px 20px;
        border-radius: 2px;
        margin-right: 10px;
        width: fit-content;

        &:focus {
            display: none;
        }
    }
}
</style>