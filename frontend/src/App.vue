<template>
    <div id="app">
        <n-loader/>
        <router-view/>
    </div>
</template>

<script>

export default {
    name: 'App',
    components: {}
}
</script>

<style lang="scss">
body {
    margin: 0;
}

#app {
}
</style>