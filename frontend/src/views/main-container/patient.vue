<template>
    <div class="flc">
        <h3>{{ title }}</h3>
        <div class="patient">
            <div></div>
            <patient-ekgs/>
        </div>
    </div>
</template>

<script>
import PatientEkgs from './sections/patient-ekgs'

export default {
    name: "patient",
    components: {PatientEkgs},
    computed: {
        getAuthUser() {
            return this.$store.getters.getAuthUser
        },
        getPatient() {
            if (this.getAuthUser.access_level === 2) {
                return this.$store.getters.getSelectedPatient
            }
            return this.$store.getters.getAuthPerson
        },
        title() {
            let middleName = this.getPatient.middle_name ? this.getPatient.middle_name : ''
            let fullName = `${this.getPatient.last_name} ${this.getPatient.first_name}
            ${middleName} (${this.getPatient.patient_id})`
            if (this.getAuthUser.access_level === 2) {
                return `Данные пациента ${fullName}`
            }
            return `Пациент ${fullName}`
        }
    }
}
</script>

<style lang="scss">
.patient {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>