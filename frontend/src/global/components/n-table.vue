<template>
    <div>
        <div class="pa-3 flс mb-10 soft-border" v-if="showFilters">
            <slot name="default"/>
            <div class="mt-5 flr">
                <n-button
                    v-if="showReloadButton"
                    @click="$emit('reloadData')"
                    :label="reloadButtonLabel"/>
                <slot name="buttons"/>
            </div>
        </div>
        <el-table class="table-class soft-border"
                  :data="tableData"
                  @row-click="(row) => $emit('rowClick', row)">
            <el-table-column v-for="(column, index) in columns"
                             :key="index"
                             :prop="column.key"
                             :label="column.title"/>
        </el-table>
    </div>

</template>

<script>
export default {
    name: "n-table",
    props: {
        tableData: {
            type: Array,
            default: () => []
        },
        columns: {
            type: Array,
            default: () => []
        },
        showFilters: {
            type: Boolean,
            default: true
        },
        showReloadButton: {
            type: Boolean,
            default: true
        },
        reloadButtonLabel: {
            type: String,
            default: "Искать"
        },
    }
}
</script>

<style lang="scss">
.table-class {
    max-height: 350px;
    overflow: auto;

    .el-table {

        &__header {
            background-color: $--color-info-lighter;

            th {
                border-left: 1px solid $--color-info-light;
                padding: 10px;
            }
        }

        &__body {
            tr {
                &:hover {
                    background-color: $--color-info-lighter;
                    cursor: pointer;
                }
            }

            .cell {
                border-left: 1px solid $--color-info-light;
                border-top: 1px solid $--color-info-light;
                padding: 7px;
            }
        }
    }
}
</style>