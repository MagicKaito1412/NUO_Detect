<template>
    <div :class="`flr mb-2 align-c ${spaceBetween ? 'justify-sb' : 'mr-' + mrNum}`">
        <span class="mr-2">{{ label }}</span>
        <el-input :class="`input-width-${250}`"
                  :readonly="readonly"
                  :show-password="password"
                  v-model="innerValue"/>
    </div>
</template>

<script>
export default {
    name: "n-input",
    props: {
        password: {
            type: Boolean,
            default: false
        },
        readonly: {
            type: Boolean,
            default: false
        },
        spaceBetween: {
            type: Boolean,
            default: true
        },
        mrNum: {
            type: Number,
            default: null
        },
        inputWidth: {
            type: Number,
            default: 250
        },
        value: {
            default: null
        },
        label: {
            type: String,
            default: ''
        }
    },
    data() {
        return {
            innerValue: null
        }
    },
    watch: {
        value(val) {
           this.$set(this, 'innerValue', val)
        },
        innerValue(val) {
            this.$emit('update:value', val)
        }
    },
}
</script>

<style scoped>

</style>