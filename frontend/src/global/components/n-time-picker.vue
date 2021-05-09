<template>
    <div :class="`fl-row mb-2 align-c ${spaceBetween ? 'justify-sb' : 'mr-' + mrNum}`">
        <span class="mr-2" v-if="label">{{ label }}</span>
        <el-time-picker
            :class="`input-width-${inputWidth}`"
            :placeholder="placeholder"
            :readonly="readonly"
            :clearable="false"
            format="HH:mm"
            value-format="HH:mm"
            v-model="innerValue"
        />
    </div>
</template>

<script>
export default {
name: "n-time-picker",
    props: {
        value: {
            default: null
        },
        placeholder: {
            type: String,
            default: 'чч:мм'
        },
        label: {
            type: String,
            default: null
        },
        spaceBetween: {
            type: Boolean,
            default: true
        },
        mrNum: {
            type: Number,
            default: null
        },
        readonly: {
            type: Boolean,
            default: false
        },
        inputWidth: {
            type: Number,
            default: 240
        },
    },
    data() {
        return {
            innerValue: null,
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