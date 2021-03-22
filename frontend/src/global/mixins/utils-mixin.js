export default {
    methods: {
        goTo(name) {
            if (this.$route.name === name) return;
            let routerData = name;
            if (typeof name === 'string') {
                routerData = {name: name}
            }
            this.$router.push(routerData)
        }
    }
}