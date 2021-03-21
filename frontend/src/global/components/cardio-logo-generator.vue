<template>
    <div>
        <div>
            <img v-for="(number, index) in arrayNumber"
                 :key="index"
                 class="cardio-logo" src="@/assets/cardiogram.png"/>
        </div>
    </div>
</template>

<script>
export default {
    name: "cardio-logo-generator",
    props: {
        number: {
            type: Number,
            default: 1
        }
    },
    computed: {
        arrayNumber() {
            let arr = []
            for (let num = 1; num <= this.number; num++) {
                    arr.push(num)
                }
            return arr
        }
    }
}
</script>

<style scoped>

</style>