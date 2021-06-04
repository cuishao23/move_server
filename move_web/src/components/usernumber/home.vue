<template>
  <div class="versionDiv">
    <div class="usernumber_tab">
      <input type="text" class="filter-text" v-model="address" placeholder="地区" onkeyup="value=value.replace(/[^\u4e00-\u9fa5]/g,'')"/>
      <el-select v-model="genderType" value="" placeholder="性别" filterable>
        <el-option
          v-for="(item,index) in genderTypes"
          :key="index"
          :label="item.text"
          :value="item.value">
        </el-option>
      </el-select>
      <button class='search' @click="searchUserInfo()"></button>
      <button class="normal-btn export" @click="onExport()">导出</button>
    </div>
    <span class="res-tip-show" id="NoDataShow">未找到匹配数据</span>
    <div id='DataShow'>
      <nms-pager-table :data="deviceList" :fields="deviceFields" :total-page="userTotalPage" :biao-zhi="cage" v-model="curPage"/>
    </div>
  </div>
</template>

<script>
  import NmsPagerTable from "../../components/common/nms-pager-table";
  import api from '../../axios'
  import {getUserInfoFields, genderTypes} from "../../assets/js/usernumber"
  import {Upexcele}  from '../common/commonFunction'


  export default {
    name: "usernumberhome",
    components: {NmsPagerTable},
    inject: ['reload'],
    data() {
      return {
        // 表格每页显示数量
        perPage: 15,
        curPage: 1,
        cage: 1,
        userTotalPage: 1,
        deviceList: [],
        deviceFields: [],
        address: '',
        genderType: 'all',
        genderTypes: genderTypes
      }
    },
    mounted() {
      api.getUserInfoList({params: {
          newPageNum: 1,
          address: this.address,
          genderType: this.genderType
        }
      }).then(res => {
        this.deviceList = res.data;
        this.deviceFields = getUserInfoFields();
        this.userTotalPage = Math.ceil(res.total_num / this.perPage);
        document.getElementById("NoDataShow").style.display = "none";
        document.getElementById("DataShow").style.display = "block";
      })
      .catch((error) => {
        console.log(error);
      })
    },
    watch: {
      curPage: function (newPageNum, oldPageNum) {
        this.cage = 1
        api.getUserInfoList({params: {
            newPageNum: newPageNum,
            address: this.address,
            genderType: this.genderType
          }
        }).then(res => {
          this.deviceList = res.data;
          this.deviceFields = getUserInfoFields();
          this.userTotalPage = Math.ceil(res.total_num / this.perPage);
          document.getElementById("NoDataShow").style.display = "none";
          document.getElementById("DataShow").style.display = "block";
        })
        .catch((error) => {
          console.log(error);
        })
      }
    },
    methods: {
      searchUserInfo: function () {
        api.getUserInfoList({params: {
            newPageNum: 1,
            address: this.address,
            genderType: this.genderType
          }
        }).then(res => {
          this.deviceList = res.data;
          this.deviceFields = getUserInfoFields();
          this.userTotalPage = Math.ceil(res.total_num / this.perPage);
          this.cage = 2
          //no according results
          if (Object.entries(res.data).length==0){
            document.getElementById("DataShow").style.display = "none";
            document.getElementById("NoDataShow").style.display = "block";
          }else{
            document.getElementById("DataShow").style.display = "block";
            document.getElementById("NoDataShow").style.display = "none";
          }
        })
        .catch((error) => {
          console.log(error);
        })
      },
      onExport: function () {
        api.getUserDownLoad({params: {
          address: this.address,
          genderType: this.genderType
        }, responseType: 'blob'}).then(res => {
          Upexcele(res, '用户实名认证表.xlsx')
        }).catch(error => {
          console.log(error)
        });
      },
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
</style>


<style>
  /* 不加scoped自定义样式*利用类下类引用解决了全局污染 */
  .second-col .el-input {
    width: 319px;
  }
</style>
