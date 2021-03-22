<template>
    <n-dialog :visible.sync="visible" :title="title" @close="close"/>
</template>

<script>
export default {
    name: "edit-doctor",
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        createMode: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        getSelectedDoctor() {
            return this.$store.getters.getSelectedDoctor
        },
        title() {
            if (this.createMode) {
                return `Регистрация нового пользователя`
            }
            let middleName = this.getSelectedDoctor.middle_name ? this.getSelectedDoctor.middle_name : ''
            let fullName = `${this.getSelectedDoctor.last_name} ${this.getSelectedDoctor.first_name}
            ${middleName} (${this.getSelectedDoctor.doctor_id})`
            return `Редактирование пользователя ${fullName}`
        }
    },
    methods: {
        close() {
            this.$emit('update:createMode', false)
            this.$emit('update:visible', false)
        }
    }
}
</script>

<style scoped>

</style>