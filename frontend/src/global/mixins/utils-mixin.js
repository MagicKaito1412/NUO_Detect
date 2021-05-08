export default {
    methods: {
        goTo(name, params = {}) {
            if (this.$route.name === name || typeof name !== 'string') return;
            let routerData = {
                name: name,
                params: params
            }
            this.$router.push(routerData)
        },

        showMessage(title, message, type = 'info', duration = 3000) {
            this.$notify({
                type: type,
                title: title,
                message: message,
                duration: duration,
                position: "top-right",
                customClass: 'custom-notification'
            })
        },
        showSMessage(title = 'Данные успешно сохранены!', message, duration) {
            this.showMessage(title, message, "success", duration);
        },
        showEMessage(title, message, duration) {
            this.showMessage(title, message, "error", duration);
        },
        showIMessage(title, message, duration) {
            this.showMessage(title, message, "info", duration);
        },
        showWMessage(title, message, duration) {
            this.showMessage(title, message, "warning", duration);
        },
    }
}