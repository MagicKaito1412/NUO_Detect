<template>
    <div class="fl-col">
        <!--   todo     https://codepen.io/seogi1004/pen/jpqNPm example for line graph-->
        <div class="fl-row justify-sb">
            <graph-bar
                v-if="genderCountValues"
                :width="600"
                :height="400"
                :axis-min="0"
                :labels="['']"
                :values="genderCountValues">
                <note text="Количество пациентов"/>
                <tooltip :names="genderNames" :position="'center'"/>
                <legends :names="genderNames"/>
            </graph-bar>
            <graph-bar
                v-if="genderAgesValues"
                :width="600"
                :height="400"
                :axis-min="0"
                :labels="['18-44', '45-64', '65+']"
                :values="genderAgesValues">
                <note text="Возрастные интервалы"/>
                <tooltip :names="genderNames" :position="'center'"/>
                <legends :names="genderNames"/>
            </graph-bar>
        </div>
        <divider/>
        <graph-pie
            v-if="nuoValues"
            :width="500"
            :height="500"
            :values="nuoValues"
            :names="nuoNames"
            :active-index="[ 0, 2 ]"
            :active-event="'click'"
            show-text-type="inside">
            <note text="Статистика о наличие НУО"/>
            <tooltip :names="nuoNames" :position="'center'"/>
            <legends :names="nuoNames"/>
        </graph-pie>
        <!--        <graph-pie-->
        <!--            :width="500"-->
        <!--            :height="500"-->
        <!--            :padding-top="100"-->
        <!--            :padding-bottom="100"-->
        <!--            :padding-left="100"-->
        <!--            :padding-right="100"-->
        <!--            :values="bmiValues"-->
        <!--            :names="bmiNames"-->
        <!--            :active-index="[ 0, 2 ]"-->
        <!--            :active-event="'click'"-->
        <!--            :show-text-type="'outside'">-->
        <!--            <note text="Индекс массы тела"/>-->
        <!--            <tooltip :names="bmiNames" :position="'center'"/>-->
        <!--            <legends :names="bmiNames"/>-->
        <!--        </graph-pie>-->
    </div>
</template>

<script>
import PatientsService from '../main-container/patient/patient-service'

export default {
    name: "statistics",
    data() {
        return {
            genderNames: ["Мужчины", "Женщины"],
            nuoNames: ["Имеют НУО", "Не имеют НУО"],
            genderCountValues: null,
            genderAgesValues: null,
            nuoValues: null,
            // bmiNames: ["16-18", "19-25", "26-30", "31-35", "36-40", "41+"],
            // bmiValues: null,
        }
    },
    created() {
        PatientsService.loadPatientStatistics().then(result => {
            if (result) {

                let statistics = result.data
                let genderCountValues = statistics.genderCountValues
                let genderAgesValues = statistics.genderAgesValues
                let nuoValues = statistics.nuoValues

                this.$set(this, 'genderCountValues', [[0], [0]])
                this.$set(this, 'genderAgesValues', [[0, 0, 0], [0, 0, 0]])
                this.$set(this, 'nuoValues', [0, 0])

                this.genderCountValues[0] = [genderCountValues['men']]
                this.genderCountValues[1] = [genderCountValues['women']]

                this.genderAgesValues[0] = genderAgesValues['men']
                this.genderAgesValues[1] = genderAgesValues['women']

                this.nuoValues[0] = nuoValues['has_nuo']
                this.nuoValues[1] = nuoValues['has_not_nuo']
            }
        })
    }
}
</script>

<style scoped>

</style>