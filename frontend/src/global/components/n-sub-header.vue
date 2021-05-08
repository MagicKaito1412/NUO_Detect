<template>
    <div>
        <divider v-if="topPosition"/>
        <h4 :class="topPosition ? 'mt-2' : 'mb-2'">{{ label }}</h4>
        <divider v-if="!topPosition"/>
    </div>
</template>

<script>
export default {
    name: "n-sub-header",
    props: {
        label: {
            type: String,
            default: ''
        },
        position: {
            type: String,
            default: 'top' //top, bottom
        }
    },
    computed: {
        topPosition() {
            return this.position === 'top'
        }
    }
}
</script>

<style scoped>

</style>