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
            default: 'primary' //primary, default, error
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
                ['error-button']: this.type === 'error',
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

    .error-button {
        background-color: $--color-danger;
        color: white;
        border: 1px solid $--color-danger-dark;

        &:hover {
            background-color: $--color-danger-dark;
        }
    }

    .disabled-button {
        background-color: $--color-primary-lighter;
        color: $--color-info-lighter;
        border: 1px solid $--color-info-light;
        text-shadow: 1px 1px 1px $--color-info;
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