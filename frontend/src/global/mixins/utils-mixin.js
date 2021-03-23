export default {
    methods: {
        goTo(name, params = null) {
            if (this.$route.name === name || typeof name !== 'string') return;
            let routerData = {
                name: name,
                params: params
            }
            this.$router.push(routerData)
        }
    }
}