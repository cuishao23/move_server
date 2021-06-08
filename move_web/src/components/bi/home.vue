<template>
  <el-tabs v-model="tabType">
    <el-tab-pane label="政府福利券" name="governmentticket" class="ticket_tab">
    </el-tab-pane>
    <el-tab-pane label="商业福利券" name="businessticket" class="ticket_tab">
    </el-tab-pane>
        <el-tab-pane label="发券评估" name="analyseticket" class="ticket_tab">
    </el-tab-pane>
        <el-tab-pane label="ROI" name="roi" class="ticket_tab">
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import api from '../../axios'

export default {
    components: {},
    name: "bihome",
    data() {
        return {
            // tab标签类型
            tabType: "governmentticket",
        };
    },
    mounted() {
      console.log('政府福利券接口...')
    },
    watch: {
        tabType: function(newTab,oldTab){
          console.log(this.tabType)
          if (newTab = "governmentticket") {
            console.log('政府福利券接口...')
          } else if (newTab = "businessticket") {
            console.log('商业福利券接口...')
          } else if (newTab = "analyseticket") {
            console.log('发券评估接口...')
          } else if (newTab = "ROI") {
            console.log('roi接口...')
          }
        }
    },
    methods: {}
};
</script>

<style scoped>
    .ticket_tab {
        text-align: left;
        padding-top: 20px;
    }
</style>
