<template>
    <div>

    </div>
</template>

<script>
import {EKG} from "../../service/models";
// import Service from "../service/service";

export default {
    name: "ekg",
    data() {
        return {
            ekg: new EKG()
        }
    },
    methods: {
        save() {
            //todo creationMode in dialog
            // Service.addEkg().then(result => )
        }
    },
    computed: {

    },
}
</script>

<style scoped>

</style>