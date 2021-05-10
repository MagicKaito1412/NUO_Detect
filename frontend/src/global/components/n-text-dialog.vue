<template>
    <n-dialog :visible="visible"
              :show-divider="false"
              :show-close-icon="false"
              :title="text"
              @close="close"
              class="n-text-dialog">
        <div class="fl-row justify-c">
            <n-button
                label="Принять"
                @click="close"/>
        </div>
    </n-dialog>
</template>

<script>
export default {
    name: "n-text-dialog",
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        text: {
            type: String,
            default: ''
        }
    },
    methods: {
        close() {
            this.$emit('update:visible', false)
        }
    }
}
</script>

<style lang="scss">
.n-text-dialog {
    .pn-form {
        width: 35%;
    }
}
</style>