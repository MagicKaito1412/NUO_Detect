<template>
    <div>
        <main-wrapper :access_level="access_level">
            <div class="pa-5">
                <router-view/>
            </div>
            <change-pass-dialog
                :visible.sync="showDialog"
                :show-close-icon="false"
                @saveButton="goToHomePage"/>
        </main-wrapper>
    </div>
</template>

<script>
import ChangePassDialog from "./change-pass-dialog";
export default {
    name: "home",
    components: {ChangePassDialog},
    data() {
        return {
            access_level: 0,
            showDialog: false
        }
    },
    methods: {
        goToHomePage() {
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
    },
    mounted() {
        let changePass = this.$route.params.changePass
        if (changePass) {
            this.$set(this, 'showDialog', true)
        } else {
            this.goToHomePage()
        }
    }
}
</script>

<style scoped>

</style>