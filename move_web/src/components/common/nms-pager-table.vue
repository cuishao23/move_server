<template>
  <div style="width: 100%;margin-top: 8px">
    <el-table :data="curData" stripe style="width: 100%" border align="left" :highlight-current-row="highLight" ref="tbl"
              @selection-change="handleSelectionChange"
              @row-click="onSelect">
      <el-table-column type="index" :index="startIndex" width="50" label="序号" v-if="index"/>
      <el-table-column v-if="selection"
                       type="selection"
                       width="55">
      </el-table-column>
      <el-table-column v-for="(item, index) in fields" :key="index" :label="item.label" :prop="item.prop"
                       :show-overflow-tooltip="true">
        <template slot-scope="scope">
          <div v-if="item.prop ==='id_type'">
            <span v-if="scope.row.id_type === 1">身份证</span>
            <span v-else-if="scope.row.id_type === 2">护照</span>
            <span v-else>---</span>
          </div>
          <div v-else-if="item.prop ==='gender'">
            <span v-if="scope.row.gender === 1">男</span>
            <span v-else-if="scope.row.gender === 2">女</span>
            <span v-else>---</span>
          </div>
          <div v-else-if="item.prop ==='state'">
            <span v-if="scope.row.state === 1">是</span>
            <span v-else-if="scope.row.state === 0">否</span>
          </div>
          <div v-else-if="item.prop ==='status'">
            <span v-if="scope.row.status === 1">有效</span>
            <span v-else-if="scope.row.status === 2">删除</span>
          </div>
          <div v-else-if="item.prop === 'app' && item.flag === 'app_type'">
            <span v-if="scope.row.app == '1'">每步赛事</span>
            <span v-else-if="scope.row.app == '12'">赛易云</span>
            <span v-else-if="scope.row.app == '7'">迈麦体育产业</span>
            <span v-else-if="scope.row.app == '10'">RunBike儿童平衡车</span>
            <span v-else-if="scope.row.app == '8'">PTSA+</span>
            <span v-else-if="scope.row.app == '6'">奔跑吧少东家</span>
            <span v-else-if="scope.row.app == '3'">每步+</span>
            <span v-else-if="scope.row.app == '2'">Campusrun跑步训练营</span>
            <span v-else-if="scope.row.app == '4'">mpms</span>
            <span v-else-if="scope.row.app == '101'">每步运动会H5</span>
            <span v-else-if="scope.row.app == '16'">五星运动汇小程序</span>
            <span v-else-if="scope.row.app == '18'">慕道无极</span>
            <span v-else-if="scope.row.app == '17'">黄浦我来赛</span>
            <span v-else-if="scope.row.app == '21'">体育锻炼达标赛</span>
            <span v-else-if="scope.row.app == '11'">赛易云h5</span>
            <span v-else-if="scope.row.app == '108'">上海市青少年体育协会</span>
            <span v-else-if="scope.row.app == '109'">第三届市民运动会配送服务平台</span>
            <span v-else-if="scope.row.app == '110'">嘉定体育</span>
            <span v-else-if="scope.row.app == '111'">全嘉运动会</span>
            <span v-else-if="scope.row.app == '112'">上海市武术世锦赛</span>
            <span v-else-if="scope.row.app == '113'">Campusrun跑步训练营</span>
            <span v-else-if="scope.row.app == '114'">松江健步走</span>
            <span v-else-if="scope.row.app == '115'">虹口 谁是联赛王</span>
            <span v-else-if="scope.row.app == '116'">汇体育</span>
            <span v-else-if="scope.row.app == '117'">泳乐趣</span>
            <span v-else-if="scope.row.app == '118'">黄浦区体育指导员</span>
            <span v-else-if="scope.row.app == '119'">高校百英里</span>
            <span v-else-if="scope.row.app == '19'">爱在每步</span>
            <span v-else-if="scope.row.app == '20'">动驿动</span>
            <span v-else-if="scope.row.app == '122'">精英挑战赛</span>
            <span v-else-if="scope.row.app == '123'">嘉定云配送</span>
            <span v-else-if="scope.row.app == '124'">上海市线上运动会</span>
            <span v-else-if="scope.row.app == '125'">翔动宝</span>
            <span v-else-if="scope.row.app == '126'">健康浦东行</span>
            <span v-else-if="scope.row.app == '127'">健身地图</span>
            <span v-else-if="scope.row.app == '128'">江湾体育场</span>
            <span v-else-if="scope.row.app == '129'">华新镇</span>
            <span v-else-if="scope.row.app == '130'">长宁小程序</span>
            <span v-else-if="scope.row.app == '131'">上海市社体 (竞赛) 中心内部管理系统</span>
            <span v-else-if="scope.row.app == '132'">普陀线上运动会</span>
            <span v-else-if="scope.row.app == '133'">云动斜土</span>
            <span v-else-if="scope.row.app == '134'">质在青浦</span>
            <span v-else-if="scope.row.app == '135'">厦门线上运动会小程序</span>
            <span v-else-if="scope.row.app == '136'">长宁区社区公共运动场</span>
            <span v-else-if="scope.row.app == '137'">培训会员h5</span>
            <span v-else-if="scope.row.app == '138'">日照体育小程序</span>
            <span v-else-if="scope.row.app == '139'">崇明休闲体育</span>
            <span v-else-if="scope.row.app == '140'">圣步</span>
            <span v-else-if="scope.row.app == '141'">漂移赛事服务系统</span>
            <span v-else-if="scope.row.app == '142'">健步赛事服务系统</span>
            <span v-else-if="scope.row.app == '143'">兰菁智慧赛事服务系统</span>
          </div>
          <div v-else>
            <span v-if="scope.row[item.prop] == null">---</span>
            <span v-else>{{ scope.row[item.prop] }}</span>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <div class="pager" v-if="pager">
      <div class="goto-page">
        <input type="text" v-model.number="curPage" @keyup.enter="_gotoPage(curPage)" oninput = "value=value.replace(/[^\d]/g,'')"/><span>/</span><span>{{ totalPage }}</span>
      </div>
      <div class="pre-next-page">
        <div class="pre-page" @click="_prePage()"></div>
        <div class="next-page" @click="_nextPage()"></div>
      </div>
    </div>
    <nms-dialog title="提示" ref="isFirstDlg" width="400px" height="152px">
       <div slot="content">
         <div class="delTipsDiv">
            <span class="PromptImg"></span>
            <span>当前页为第一页</span>
         </div>
       </div>
    </nms-dialog>
    <nms-dialog title="提示" ref="isLastDlg" width="400px" height="152px">
      <div slot="content">
        <div class="delTipsDiv">
          <span class="PromptImg"></span>
          <span>当前页为最后一页</span>
        </div>
      </div>
    </nms-dialog>
    <nms-dialog title="提示" ref="wrongPageNum" width="400px" height="152px">
      <div slot="content">
        <div class="delTipsDiv">
          <span class="PromptImg"></span>
          <span>页码超过范围</span>
        </div>
      </div>
    </nms-dialog>
  </div>
</template>

<script>
  import NmsDialog from "./nms-dialog";
  import $ from 'jquery'

  export default {
    components: {NmsDialog},
    name: "nms-pager-table",
    data() {
      return {
        curPage: 1,
        startIndex: 1,
        currentSelect: null,
        highLight: true,
        curData: [],
        multipleSelection: null,
        a: false
      }
    },
    model: {
      prop: 'multipleSelection',
      event: 'multiSelect',

      prop: 'curPage',
      event: 'curPage'
    },
    created: function () {
      if (this.data != null && this.data.length > 0) {
        this.sliceData(1)
      } else {
        this.curPage = 1
      }
    },
    watch: {
      curPage: function (newPageNum, oldPageNum) {
        if (newPageNum > this.totalPage) {
          this.$refs.wrongPageNum.open()
          this.curPage=1
          this.$emit('curPage', this.curPage);
          this.startIndex = (this.curPage - 1) * this.perPage + 1
          return
        }
        this.curPage = newPageNum
        if(this.biaoZhi==2){
          this.$emit('curPage', this.curPage);
          this.startIndex = (newPageNum - 1) * this.perPage + 1
        }
      },
      data: function (newData, oldData) {
        if (this.biaoZhi == 2) {
          this.curPage=1
        }
        this.sliceData(this.curPage)

      },
    },
    methods: {
      sliceData: function (pageNum) {
        if (pageNum > this.totalPage || pageNum < 1) {
          return
        }
        let data = this.data
        if (data.length !== 0) {
          this.curData = data
          this.curPage = pageNum
        }
      },
      _prePage: function () {
        if (this.curPage === 1 || this.curPage === 0) {
          this.$refs.isFirstDlg.open()
          this.curPage=1
          this.$emit('curPage', this.curPage);
          this.startIndex = (this.curPage - 1) * this.perPage + 1
          return
        }
        let pageNum = this.curPage - 1
        this.$emit('curPage', pageNum);
        this.startIndex = (pageNum - 1) * this.perPage + 1
        if (this.prePage == null) {
          if (this.curPage > 1) {
            this.sliceData(this.curPage - 1)
          }
        } else {
          let data = this.prePage(pageNum)
          if (data !== null && data.length > 0) {
            this.curData = data
            this.curPage = pageNum
          }
        }
      },
      _nextPage: function () {
        if (this.curPage === this.totalPage) {
          this.$refs.isLastDlg.open()
          this.curPage=1
          this.$emit('curPage', this.curPage);
          this.startIndex = (this.curPage - 1) * this.perPage + 1
          return
        }
        let pageNum = this.curPage + 1
        this.$emit('curPage', pageNum);
        this.startIndex = (pageNum-1) * this.perPage + 1
        if (this.nextPage == null) {
          if (this.curPage < this.totalPage) {
            this.sliceData(this.curPage + 1)
          }
        } else {
          let data = this.nextPage(pageNum)
          if (data !== null && data.length > 0) {
            this.curData = data
            this.curPage = pageNum
          }
        }
      },
      _gotoPage: function (pageNum) {
        if (pageNum < 1 || pageNum > this.totalPage) {
          this.$refs.wrongPageNum.open()
          this.curPage=1
          this.$emit('curPage', this.curPage);
          this.startIndex = (this.curPage - 1) * this.perPage + 1
          return
        }else{
          this.$emit('curPage', this.curPage);
          this.startIndex = (pageNum - 1) * this.perPage + 1
        }
        if (this.gotoPage == null) {
          this.sliceData(pageNum)
        }
      },
      onSelect: function (row, event, column) {
        this.multipleSelection = row;
        this.$emit('multiSelect', this.multipleSelection)
        if (this.selection === true) {
          this.highLight = false
          this.$refs.tbl.toggleRowSelection(row)
        } else {
          if (this.currentSelect === row) {
            this.$refs.tbl.clearSelection()
            this.currentSelect = null
            this.highLight = false
          } else {
            this.currentSelect = row
            this.highLight = true
          }
        }
        if (this.rowClick != null) {
          this.rowClick(row)
        }
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
        this.$nextTick(() => {
          $('tbody tr', this.$el).each(function (index, ele) {
            let checkedTd = $('td.el-table-column--selection .is-checked', ele)
            if (checkedTd.length === 0) {
              $('td', ele).removeClass('td-black')
            } else {
              $('td', ele).addClass('td-black')
            }
          })
        })
        console.log('send multi select: ' + JSON.stringify(this.multipleSelection))
        this.$emit('multiSelect', this.multipleSelection)
        this.$store.commit('change',this.multipleSelection)
      }
    },
    props: {
      fields: {
        type: Array,
        required: true
      },
      totalPage: {
        type: Number
      },
      biaoZhi: {
        type: Number
      },
      perPage: {
        type: Number,
        default: function () {
          return 15
        }
      },
      pager: {
        type: Boolean,
        default: function () {
          return true
        }
      },
      index: {
        type: Boolean,
        default: function () {
          return true
        }
      },
      selection: {
        type: Boolean,
        default: function () {
          return false
        }
      },
      data: {
        type: Array,
        default: function () {
          return []
        }
      },
      rowClick: {
        type: Function
      },
      gotoPage: {
        type: Function
      },
      prePage: {
        type: Function
      },
      nextPage: {
        type: Function
      }
    }
  }
</script>

<style scoped>
  .pre-page, .next-page {
    width: 21px;
    height: 20px;
    cursor: pointer;
    position: relative;
    top: 1px;
  }

  .pager {
    float: right;
  }

  .goto-page {
    margin-right: 5px;
    float: left;
  }

  .goto-page input {
    width: 25px;
    padding-bottom: 0px;
  }

  .goto-page span {
    font-size: 11px;
    padding-left: 5px;
  }

  .pre-next-page {
    width: 42px;
    float: right;
  }

  .pre-page {
    float: left;
    background: url(../../assets/image/list_prepage.png);
  }

  .pre-page:hover {
    background: url(../../assets/image/list_prepage.png) -21px 0;
  }

  .pre-page:active {
    background: url(../../assets/image/list_prepage.png) -42px 0;
  }

  .next-page {
    float: right;
    background: url(../../assets/image/list_nextpage.png);
  }

  .next-page:hover {
    background: url(../../assets/image/list_nextpage.png) -21px 0;
  }

  .next-page:active {
    background: url(../../assets/image/list_nextpage.png) -42px 0;
  }
  
  .pager {
    position: fixed;
    bottom: 30px;
    right: 120px;
  }

  .note-content {
    font-size: 12px;
    color: #4e4e4e;
    white-space: nowrap;
    overflow: auto;
    height: 21px;
    line-height: 21px;
    background: url(../../assets/image/prompt.png) no-repeat;
    padding-left: 30px;
  }
  .el-table .cell.el-tooltip div {
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .delTipsDiv {
    text-align: center;
    padding-top: 50px;
  }
</style>
