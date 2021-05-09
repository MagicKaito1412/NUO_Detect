import GraphLine from 'vue-graph/src/components/line'
import GraphBar from 'vue-graph/src/components/bar'
import GraphPie from 'vue-graph/src/components/pie'
import WidgetTooltip from 'vue-graph/src/widgets/tooltip'
import WidgetLegends from 'vue-graph/src/widgets/legends'
import WidgetGuideline from 'vue-graph/src/widgets/guideline'
import WidgetNote from 'vue-graph/src/widgets/note'

export default {
    install(Vue) {
        Vue.component(GraphLine.name, GraphLine)
        Vue.component(GraphBar.name, GraphBar)
        Vue.component(GraphPie.name, GraphPie)
        Vue.component(WidgetTooltip.name, WidgetTooltip)
        Vue.component(WidgetLegends.name, WidgetLegends)
        Vue.component(WidgetGuideline.name, WidgetGuideline)
        Vue.component(WidgetNote.name, WidgetNote)
    }
}