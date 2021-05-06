<template>
    <div :class="`flr mb-2 align-c ${spaceBetween ? 'justify-sb' : 'mr-' + mrNum}`">
        <span class="mr-2" v-if="label">{{ label }}</span>
        <el-date-picker
            :class="`input-width-${inputWidth}`"
            :placeholder="placeholder"
            :readonly="readonly"
            :clearable="false"
            :picker-options="pickerOptions"
            format="dd.MM.yyyy"
            v-model="innerValue"
        />
    </div>
</template>

<script>
 import moment from 'moment';

export default {
    name: "n-date-picker",
    props: {
        value: {
            default: null
        },
        placeholder: {
            type: String,
            default: 'дд.мм.гггг'
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
            time1: null,
        time2: null,
        time3: null,
        }
    },
    computed: {
        pickerOptions() {
                return {
                    firstDayOfWeek: 1,
                    cellClassName: (date) => {
                        if ([6, 7].includes(moment(date).isoWeekday())) {
                            return 'm-cell m-cell--weekend'
                        }
                        return 'm-cell'
                    }
                }
            },
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