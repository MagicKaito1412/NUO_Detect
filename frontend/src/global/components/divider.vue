<template>
    <div :class="type === 'horizontal' ? 'divider' : 'vertical-divider'"/>
</template>

<script>
export default {
    name: "divider",
    props: {
        type: {
            type: String,
            default: 'horizontal' //horizontal, vertical
        }
    }
}
</script>

<style lang="scss">
.divider {
    background-color: $--color-primary;
    height: 4px;
    margin: 4px 0;
}

.vertical-divider {
    background-color: $--color-secondary-light;
    width: 2px;
    margin: 0 15px;
}
</style>