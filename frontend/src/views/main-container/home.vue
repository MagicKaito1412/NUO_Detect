<template>
    <div>
        <main-wrapper :access_level="access_level">
            <div class="pa-5">
                <router-view/>
            </div>
        </main-wrapper>
    </div>
</template>

<script>
export default {
    name: "home",
    data() {
        return {
            access_level: 0
        }
    },
    mounted() {
        let authUser = this.$store.getters.getAuthUser
        this.$set(this, 'access_level', authUser.access_level)
        if (this.access_level === 1) { //super user
            this.goTo('doctors')
        } else if (this.access_level === 2) { //doctor
            this.goTo('patients')
        } else if (this.access_level === 3) { //patient
            this.goTo('patient')
        }
    }
}
</script>

<style scoped>

</style>