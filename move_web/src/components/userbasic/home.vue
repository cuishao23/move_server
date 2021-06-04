<template>
  <div class="versionDiv">
    <div class="usernumber_tab">
      <input type="text" class="filter-text" v-model="address" placeholder="地区" onkeyup="value=value.replace(/[^\a-\z\A-\Z\u4E00-\u9FA5]/g,'')"/>
      <el-select v-model="genderType" value="" placeholder="性别" filterable>
        <el-option
          v-for="(item,index) in genderTypes"
          :key="index"
          :label="item.text"
          :value="item.value">
        </el-option>
      </el-select>
      <el-select v-model="appType" value="" placeholder="赛事" filterable>
        <el-option
          v-for="(item,index) in appTypes"
          :key="index"
          :label="item.text"
          :value="item.value">
        </el-option>
      </el-select>
      <button class='search' @click="searchUserInfo()"></button>
      <button class="normal-btn export" @click="onExport()">导出</button>
    </div>
    <span class="res-tip-show" id="TipShow">数据查询中...</span>
    <span class="res-tip-show" id="NoDataShow">未找到匹配数据</span>
    <div id="DataShow">
      <nms-pager-table :data="userBasicList" :fields="userBasicFields" :total-page="userTotalPage" :biao-zhi="cage" v-model="curPage"/>
    </div>
  </div>
</template>

<script>
  import NmsPagerTable from "../../components/common/nms-pager-table";
  import api from '../../axios'
  import {getUserBasicFields, genderTypes, appTypes} from "../../assets/js/usernumber"
  import {Upexcele}  from '../common/commonFunction'


  export default {
    name: "userbasichome",
    components: {NmsPagerTable},
    inject: ['reload'],
    data() {
      return {
        // 表格每页显示数量
        perPage: 15,
        curPage: 1,
        cage: 1,
        userTotalPage: 999,
        userBasicList: [],
        userBasicFields: [],
        address: '',
        genderType: 'all',
        genderTypes: genderTypes,
        appType: 'all',
        appTypes: appTypes
      }
    },
    mounted() {
      document.getElementById("TipShow").style.display = "block";
      document.getElementById("NoDataShow").style.display = "none";
      document.getElementById("DataShow").style.display = "none";
      api.getUserBasicInfoList({params: {
          newPageNum: 1,
          address: this.address,
          genderType: this.genderType,
          appType: this.appType
        }
      }).then(res => {
        this.userBasicList = res.data;
        this.userBasicFields = getUserBasicFields();
        document.getElementById("NoDataShow").style.display = "none";
        document.getElementById("TipShow").style.display = "none";
        document.getElementById("DataShow").style.display = "block";
      })
      .catch((error) => {
        console.log(error);
      })
      this.getTotalPagenum()
    },
    watch: {
      curPage: function (newPageNum, oldPageNum) {
        document.getElementById("NoDataShow").style.display = "none";
        document.getElementById("TipShow").style.display = "block";
        document.getElementById("DataShow").style.display = "none";
        this.cage = 1
        api.getUserBasicInfoList({params: {
            newPageNum: newPageNum,
            address: this.address,
            genderType: this.genderType,
            appType: this.appType
          }
        }).then(res => {
          this.userBasicList = res.data;
          this.userBasicFields = getUserBasicFields();
          document.getElementById("NoDataShow").style.display = "none";
          document.getElementById("TipShow").style.display = "none";
          document.getElementById("DataShow").style.display = "block";
        })
        .catch((error) => {
          console.log(error);
        })
      }
    },
    methods: {
      searchUserInfo: function () {
        document.getElementById("TipShow").style.display = "block";
        document.getElementById("DataShow").style.display = "none";
        document.getElementById("NoDataShow").style.display = "none";
        api.getUserBasicInfoList({params: {
            newPageNum: 1,
            address: this.address,
            genderType: this.genderType,
            appType: this.appType
          }
        }).then(res => {
          this.userBasicList = res.data;
          this.userBasicFields = getUserBasicFields();
          this.cage = 2
          //no according results
          if (Object.entries(res.data).length==0){
            document.getElementById("TipShow").style.display = "none";
            document.getElementById("DataShow").style.display = "none";
            document.getElementById("NoDataShow").style.display = "block";
          }else{
            document.getElementById("TipShow").style.display = "none";
            document.getElementById("DataShow").style.display = "block";
            document.getElementById("NoDataShow").style.display = "none";
          }
          this.getTotalPagenum()
        })
        .catch((error) => {
          console.log(error);
        })
      },
      onExport: function () {
        api.getUserBasicDownLoad({params: {
          address: this.address,
          genderType: this.genderType,
          appType: this.appType
        }, responseType: 'blob'}).then(res => {
          Upexcele(res, '用户基本信息表.xlsx')
        }).catch(error => {
          console.log(error)
        });
      },
      getTotalPagenum: function () {
        api.getTotalPageNum({params: {
            address: this.address,
            genderType: this.genderType,
            appType: this.appType
          }
        }).then(res => {
          this.userTotalPage = Math.ceil(res.total_num / this.perPage)
        })
        .catch((error) => {
          console.log(error);
        })
      }
    }
  }
</script>

<style scoped>
  .versionDiv {
    text-align: left;
  }
  .first-col {
    width: 87px;
  }
  .second-col {
    width: 319px;
    margin-right: 15px;
  }
  .second-col input[type='text'] {
    width: 319px;
  }
  .el-input {
    width: 319px;
  }
  .first-col .note {
    font-size: 11px;
    color: #8b8b8b;
  }
  .with-textarea .first-col {
    vertical-align: top;
  }
  .normal-btn {
    float: right;
  }
  .usernumber_tab {
    padding-bottom: 5px;
  }
  .res-tip-show{
    padding-top: 100px;
    text-align: center;
    height: 320px;
    display: none;
  }
</style>


<style>
  /* 不加scoped自定义样式*利用类下类引用解决了全局污染 */
  .second-col .el-input {
    width: 319px;
  }
</style>
