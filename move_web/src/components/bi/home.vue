<template>
  <div>
    <el-tabs v-model="tabType">
      <el-tab-pane label="政府福利券" name="governmentticket" class="ticket_tab">
        <!-- <el-row :gutter="20">
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie1_option" key="pie1" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie2_option" key="pie2" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie3_option" key="pie3" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie4_option" key="pie4" />
            </div>
          </el-col>
        </el-row> -->
      </el-tab-pane>
      <el-tab-pane label="商业福利券" name="businessticket" class="ticket_tab">
        <!-- <el-row :gutter="20">
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie5_option" key="pie5" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie6_option" key="pie6" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie7_option" key="pie7" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie8_option" key="pie8" />
            </div>
          </el-col>
        </el-row> -->
      </el-tab-pane>
      <el-tab-pane label="发券评估" name="analyseticket" class="ticket_tab">
        <!-- <el-row :gutter="20">
          <el-col :span="12">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="column_option" key="column" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie9_option" key="pie9" />
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="pie10_option" key="pie10" />
            </div>
          </el-col>
        </el-row> -->
      </el-tab-pane>
      <el-tab-pane label="ROI" name="roi" class="ticket_tab">
        <!-- <el-row :gutter="20">
          <el-col>
            <div class="grid-content bg-purple">
              <v-chart class="chart" :option="roi_option" key="roi" />
            </div>
          </el-col>
        </el-row> -->
      </el-tab-pane>
    </el-tabs>

    <!-- governmentticket charts -->
    <el-row v-if="tabType === 'governmentticket'" :gutter="20">
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie1_option" key="pie1" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie2_option" key="pie2" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie3_option" key="pie3" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie4_option" key="pie4" />
        </div>
      </el-col>
    </el-row>

    <!-- businessticket charts -->
    <el-row v-else-if="tabType === 'businessticket'" :gutter="20">
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie5_option" key="pie5" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie6_option" key="pie6" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie7_option" key="pie7" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie8_option" key="pie8" />
        </div>
      </el-col>
    </el-row>

    <!-- analyseticket charts -->
    <el-row v-else-if="tabType === 'analyseticket'" :gutter="20">
      <el-col :span="12">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="column_option" key="column" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie9_option" key="pie9" />
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="pie10_option" key="pie10" />
        </div>
      </el-col>
    </el-row>

    <!-- roi charts -->
    <el-row v-else :gutter="20">
      <el-col>
        <div class="grid-content bg-purple">
          <v-chart class="chart" :option="roi_option" key="roi" />
        </div>
      </el-col>
    </el-row>

  </div>
</template>


<script>
import api from "../../axios";
import VChart, { THEME_KEY } from "vue-echarts";


export default {
  components: { VChart },
  provide: {
    [THEME_KEY]: "red",
  },
  name: "bihome",
  data() {
    return {
      // tab标签类型
      tabType: "governmentticket",
      graphInfo: {},
      pie1_option: {},
      pie2_option: {},
      pie3_option: {},
      pie4_option: {},
      pie5_option: {},
      pie6_option: {},
      pie7_option: {},
      pie8_option: {},
      column_option: {},
      pie9_option: {},
      pie10_option: {},
      roi_option: {},
    };
  },
  mounted() {
    this.initChart();
  },
  watch: {
    tabType: function (newTab, oldTab) {
      console.log(this.tabType);
      if ((newTab = "governmentticket")) {
        this.initChart();
        console.log("政府福利券接口...");
      } else if ((newTab = "businessticket")) {
        this.initChart();
        console.log("商业福利券接口...");
      } else if ((newTab = "analyseticket")) {
        this.initChart();
        console.log("发券评估接口...");
      } else if ((newTab = "ROI")) {
        this.initChart();
        console.log("roi接口...");
      }
    },
  },
  methods: {
    initChart() {
      api
        .getGraphInfo({
          params: {
            tab: this.tabType,
          },
        })
        .then((res) => {
          // console.log('resdata: '+res.data)
          this.graphInfo = res.data;
          //governmentticket图
          if (this.tabType == "governmentticket") {
            this.pie1_option = {
              title: {
                text: "用户周活比例/人数",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "用户周活比例/人数",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_active_user"],
                      name: "mock_active_user",
                    },
                    {
                      value: this.graphInfo["mock_total_user"],
                      name: "mock_total_user",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            this.pie2_option = {
              title: {
                text: "领券人数/人周活数",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "领券人数/人周活数",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_coupon_user"],
                      name: "mock_coupon_user",
                    },
                    {
                      value: this.graphInfo["mock_active_user"],
                      name: "mock_active_user",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            this.pie3_option = {
              title: {
                text: "用券人比例",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "用券人比例",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_use_coupon_user"],
                      name: "mock_use_coupon_user",
                    },
                    {
                      value: this.graphInfo["mock_coupon_user"],
                      name: "mock_coupon_user",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            this.pie4_option = {
              title: {
                text: "销券占比",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "销券占比",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_use_coupon_total"],
                      name: "mock_use_coupon_total",
                    },
                    {
                      value: this.graphInfo["mock_coupon_total"],
                      name: "mock_coupon_total",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
          }
          //businessticket图
          else if (this.tabType == "businessticket") {
            this.pie5_option = {
              title: {
                text: "用户周活比例/人数",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "用户周活比例/人数",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_active_user"],
                      name: "mock_active_user",
                    },
                    {
                      value: this.graphInfo["mock_total_user"],
                      name: "mock_total_user",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            this.pie6_option = {
              title: {
                text: "领券人数/人周活数",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "领券人数/人周活数",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_coupon_user"],
                      name: "mock_coupon_user",
                    },
                    {
                      value: this.graphInfo["mock_active_user"],
                      name: "mock_active_user",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            this.pie7_option = {
              title: {
                text: "用券人比例",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "用券人比例",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_use_coupon_user"],
                      name: "mock_use_coupon_user",
                    },
                    {
                      value: this.graphInfo["mock_coupon_user"],
                      name: "mock_coupon_user",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            this.pie8_option = {
              title: {
                text: "销券占比",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "销券占比",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo["mock_use_coupon_total"],
                      name: "mock_use_coupon_total",
                    },
                    {
                      value: this.graphInfo["mock_coupon_total"],
                      name: "mock_coupon_total",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
          }
          //analyseticket图
          else if (this.tabType == "analyseticket") {
            //横柱状图
            this.column_option = {
              title: {
                text: "福利券发放效果评估",
                subtext: "政府福利，商业福利，领取比例对照",
              },
              tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: "shadow",
                },
              },
              legend: {
                data: ["商业福利领用比例", "政府福利领用比例", "周活用户比例"],
              },
              grid: {
                left: "3%",
                right: "4%",
                bottom: "3%",
                containLabel: true,
              },
              xAxis: {
                type: "value",
                boundaryGap: [0, 0.01],
              },
              yAxis: {
                type: "category",
                data: this.graphInfo.yAxis,
              },
              series: [
                {
                  name: "商业福利领用比例",
                  type: "bar",
                  data: this.graphInfo.bus,
                },
                {
                  name: "政府福利领用比例",
                  type: "bar",
                  data: this.graphInfo.gov,
                },
                {
                  name: "周活用户比例",
                  type: "bar",
                  data: this.graphInfo.active,
                },
              ],
            };
            //饼图
            this.pie9_option = {
              title: {
                text: "政府券领取比例",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "政府券领取比例",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo.pct_data.mock_gov_given_coupon,
                      name: "mock_gov_given_coupon",
                    },
                    {
                      value: this.graphInfo.pct_data.mock_gov_prepared_coupon,
                      name: "mock_gov_prepared_coupon",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            this.pie10_option = {
              title: {
                text: "商业福利券领取比例",
                left: "center",
              },
              tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)",
              },
              series: [
                {
                  name: "商业福利券领取比例",
                  type: "pie",
                  radius: "55%",
                  center: ["50%", "60%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: "{c}\n({d}%)",
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "15px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  data: [
                    {
                      value: this.graphInfo.pct_data.mock_bus_given_coupon,
                      name: "mock_bus_given_coupon",
                    },
                    {
                      value: this.graphInfo.pct_data.mock_bus_prepared_coupon,
                      name: "mock_bus_prepared_coupon",
                    },
                  ],
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
          }
          //ROI图
          else {
            this.roi_option = {
              tooltip: {
                trigger: "item",
              },
              legend: {
                top: "5%",
                left: "center",
              },
              title: {
                text: "ROI = " + this.graphInfo.roi,
                left: "center",
                top: "center",
                textStyle: {
                  color: "#d0d1d8",
                  fontSize: 30,
                  align: "center",
                },
              },
              series: [
                {
                  name: "ROI",
                  type: "pie",
                  radius: ["40%", "70%"],
                  itemStyle: {
                    normal: {
                      label: {
                        show: true,
                        position: "inner",
                        formatter: function (params) {
                          return params.value;
                        },
                        color: "#fff",
                        fontWeight: "bold",
                        fontSize: "20px",
                      },
                      labelLine: {
                        show: false,
                      },
                    },
                  },
                  avoidLabelOverlap: false,
                  label: {
                    show: false,
                    position: "center",
                    formatter: "ROI",
                    textStyle: {
                      fontWeight: "bold",
                      fontSize: 30,
                      color: "#d0d1d8",
                    },
                  },
                  labelLine: {
                    show: false,
                  },
                  data: [
                    {
                      value: this.graphInfo.mock_gov_coupon,
                      name: "政府券金额",
                    },
                    {
                      value: this.graphInfo.mock_bus_coupon,
                      name: "商业券金额",
                    },
                    {
                      value: this.graphInfo.mock_site_cost,
                      name: "场馆消费金额",
                    },
                    {
                      value: this.graphInfo.mock_bus_cost,
                      name: "商业消费金额",
                    },
                  ],
                },
              ],
            };
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.ticket_tab {
  text-align: left;
  padding-top: 20px;
}
.el-row {
  margin-bottom: 20px;
  /* &:last-child {
    margin-bottom: 0;
  } */
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
/* .bg-purple {
  background: #d3dce6;
} */
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  height: 400px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
