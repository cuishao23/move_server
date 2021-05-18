<template>
  <div class="versionDiv">
    <div class="usernumber_tab">
      <button class="normal-btn export" @click="onExport()">导出</button>
    </div>
    <div class="table_info">
      <nms-pager-table :data="userMobileList" :fields="userMobileFields" :total-page="userTotalPage" :biao-zhi="cage" v-model="curPage"/>
    </div>
  </div>
</template>

<script>
  import NmsPagerTable from "../../components/common/nms-pager-table";
  import api from '../../axios'
  import {getUserMobileInfoFields} from "../../assets/js/usernumber"
  import {Upexcele}  from '../common/commonFunction'


  export default {
    name: "usermobilehome",
    components: {NmsPagerTable},
    inject: ['reload'],
    data() {
      return {
        // 表格每页显示数量
        perPage: 15,
        curPage: 1,
        cage: 1,
        userTotalPage: 1,
        userMobileList: [],
        userMobileFields: []
      }
    },
    mounted() {
      api.getUserMobileInfoList({params: {
          newPageNum: 1
        }
      }).then(res => {
        this.userMobileList = res.data;
        this.userMobileFields = getUserMobileInfoFields();
        this.userTotalPage = Math.ceil(res.total_num / this.perPage);
      })
      .catch((error) => {
        console.log(error);
      })
    },
    watch: {
      curPage: function (newPageNum, oldPageNum) {
        this.cage = 1
        api.getUserMobileInfoList({params: {
            newPageNum: newPageNum
          }
        }).then(res => {
          this.userMobileList = res.data;
          this.userMobileFields = getUserMobileInfoFields();
          this.userTotalPage = Math.ceil(res.total_num / this.perPage);
        })
        .catch((error) => {
          console.log(error);
        })
      }
    },
    methods: {
      onExport: function () {
        api.getUserMobileDownLoad({
          responseType: 'blob'
        }).then(res => {
          Upexcele(res, '用户号码表.xlsx')
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
  .table_info {
    padding-top: 35px;
  }
</style>


<style>
  /* 不加scoped自定义样式*利用类下类引用解决了全局污染 */
  .second-col .el-input {
    width: 319px;
  }
</style>
