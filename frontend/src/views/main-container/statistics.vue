<template>
    <div class="fl-col">
        <div class="fl-row justify-sb">
            <graph-bar
                v-if="genderCountValues"
                :width="300"
                :height="400"
                :bar-padding="30"
                :bar-margin="30"
                :axis-min="0"
                :labels="['']"
                :values="genderCountValues">
                <note text="Количество пациентов"/>
                <tooltip :names="genderNames" :position="'center'"/>
                <legends :names="genderNames"/>
            </graph-bar>
            <graph-bar
                v-if="genderAgesValues"
                :width="500"
                :height="400"
                :bar-margin="20"
                :bar-padding="5"
                :axis-min="0"
                :labels="['18-44', '45-64', '65+']"
                :values="genderAgesValues">
                <note text="Возрастные интервалы"/>
                <tooltip :names="genderNames" :position="'center'"/>
                <legends :names="genderNames"/>
            </graph-bar>
            <graph-bar
                v-if="genderNuoValues"
                :width="400"
                :height="400"
                :bar-margin="20"
                :bar-padding="5"
                :axis-min="0"
                :labels="nuoNames"
                :values="genderNuoValues">
                <note text="Гендерная статистика НУО"/>
                <tooltip :names="genderNames" :position="'center'"/>
                <legends :names="genderNames"/>
            </graph-bar>
        </div>
        <divider/>
        <graph-pie
            v-if="nuoValues"
            :width="400"
            :height="400"
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
            genderNuoValues: null,
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
                let genderNuoValues = statistics.genderNuoValues
                let nuoValues = statistics.nuoValues

                this.$set(this, 'genderCountValues', new Array(2))
                this.$set(this, 'genderAgesValues', [new Array(2)])
                this.$set(this, 'genderNuoValues', [new Array(2)])
                this.$set(this, 'nuoValues', new Array(2))

                this.genderCountValues[0] = [genderCountValues['men']]
                this.genderCountValues[1] = [genderCountValues['women']]

                this.genderAgesValues[0] = genderAgesValues['men']
                this.genderAgesValues[1] = genderAgesValues['women']

                this.genderNuoValues[0] = genderNuoValues['men']
                this.genderNuoValues[1] = genderNuoValues['women']

                this.nuoValues[0] = nuoValues['has_nuo']
                this.nuoValues[1] = nuoValues['has_not_nuo']
            }
        })
    }
}
</script>

<style scoped>

</style>