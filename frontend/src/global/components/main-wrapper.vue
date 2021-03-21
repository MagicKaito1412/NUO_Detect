<template>
    <div>
        <div class="colored-header">
            <cardio-logo-generator :number="3"/>
            <div class="colored-header __header">
                <img class="main-logo" src="@/assets/search_logo.png"/>
                <h2>Предиктивная система определения наличия НУО</h2>
            </div>
            <cardio-logo-generator :number="3"/>
        </div>
        <slot name="default"/>
        <div class="colored-header __footer">
            <h4 class="ma-1">НИУ ВШЭ, 2021</h4>
        </div>
    </div>
</template>

<script>
export default {
    name: "main-wrapper",
}
</script>

<style lang="scss">
.colored-header {
    background-color: $--color-primary;
    color: white;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    &.__footer {
        position: absolute;
        justify-content: center;
        bottom: 0;
        width: 100%;
    }

    &.__header {
        justify-content: center;

        .main-logo {
            margin-right: 10px;
            max-width: 50px;
        }
    }

    .cardio-logo {
        max-width: 100px;
    }
}
</style>