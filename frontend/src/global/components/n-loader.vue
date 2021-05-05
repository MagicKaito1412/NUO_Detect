<template>
    <div class="n-loader" v-if="isActive">
        <img class="loading-icon" src="@/assets/loading.gif"/>
    </div>
</template>

<script>
export default {
    name: "n-loader",
    computed: {
        isActive() {
            return this.$store.getters.getProgress;
        }
    }
}
</script>

<style lang="scss">
.n-loader {
    position: fixed;
    height: 100%;
    width: 100%;
    top: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.11);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 5000;
}

.loading-icon {
    height: 80px;
}

</style>