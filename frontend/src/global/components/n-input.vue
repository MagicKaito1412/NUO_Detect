<template>
    <div :class="`flr mb-2 align-c ${spaceBetween ? 'justify-sb' : 'mr-' + mrNum}`">
        <span class="mr-2" v-if="label">{{ label }}</span>
        <el-input :class="`input-width-${inputWidth}`"
                  :readonly="readonly"
                  :type="type"
                  :placeholder="placeholder"
                  :maxlength="maxlength"
                  :show-password="password"
                  v-mask="mask"
                  v-model="innerValue"
                  v-if="mask"/>
        <el-input :class="`input-width-${inputWidth}`"
                  :readonly="readonly"
                  :type="type"
                  :placeholder="placeholder"
                  :maxlength="maxlength"
                  :show-password="password"
                  v-model="innerValue"
                  v-else/>
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
            default: 240
        },
        maxlength: {
            type: Number,
            default: 250
        },
        value: {
            default: null
        },
        label: {
            type: String,
            default: null
        },
        type: {
            type: String,
            default: ''
        },
        placeholder: {
            type: String,
            default: ''
        },
        mask: {
            type: String,
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