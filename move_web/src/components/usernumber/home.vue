<template>
  <div class="versionDiv">
    <div>
      <nms-pager-table :data="deviceList" :fields="deviceFields" :total-page="userTotalPage" v-model="curPage"/>
    </div>
  </div>
</template>

<script>
  import NmsPagerTable from "../../components/common/nms-pager-table";
  import api from '../../axios'
  import {getUserInfoFields} from "../../assets/js/usernumber"
  import axios from 'axios'


  export default {
    name: "usernumber",
    components: {NmsPagerTable},
    inject: ['reload'],
    data() {
      return {
        // 表格每页显示数量
        perPage: 10,
        curPage: 1,
        cage: 1,
        userTotalPage: 1,
        deviceList: [],
        deviceFields: []
      }
    },
    mounted() {
      api.getUserInfoList({params: {
          newPageNum: 1
        }
      }).then(res => {
        this.deviceList = res.data;
        this.deviceFields = getUserInfoFields();
        this.userTotalPage = Math.ceil(res.total_num / this.perPage);
      })
      .catch((error) => {
        console.log(error);
      })
    },
    watch: {
      curPage: function (newPageNum, oldPageNum) {
        this.cage = 1
        api.getUserInfoList({params: {
            newPageNum: newPageNum
          }
        }).then(res => {
          this.deviceList = res.data;
          this.deviceFields = getUserInfoFields();
          this.userTotalPage = Math.ceil(res.total_num / this.perPage);
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
  .searchDiv{
    position: relative;
    height: 33px;
    margin-bottom: 14px;
  }
  .uploadBtn {
    position: absolute;
    right: 0;
    top: 0;
  }
  .item-list {
    color: #4e4e4e;
    font-size: 0;
    margin-left: 3px;
    margin-bottom: 27px;
  }
  .item-list li {
    font-size: 12px;
    display: inline-block;
    vertical-align: middle;
  }
  .first-col {
    width: 87px;
  }
  .version-info {
    padding-left: 30px;
    padding-top: 30px;
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
  /* .select-file {
    display: block;
    width: 30px;
    height: 30px;
    background: url(../assets/image/open_file.png);
  } */
  .without-first-col {
    margin-left: 90px;
    margin-bottom: 27px;
    font-size: 0;
  }
  #start_upload {
    margin-top: -7px;
    margin-right: 15px;
  }
  .first-col .note {
    font-size: 11px;
    color: #8b8b8b;
  }
  .with-textarea .first-col {
    vertical-align: top;
  }
  /* #select_users {
    display: block;
    width: 30px;
    height: 30px;
    background: url(../assets/image/btn-select.png);
  } */
  /* #add_ter_num {
    display: block;
    width: 30px;
    height: 30px;
    background: url(../assets/image/add.png);
  } */
  #ter_num_list {
    margin-top: -7px;
  }
  .without-first-col li {
    font-size: 12px;
    display: inline-block;
    vertical-align: middle;
  }
  .ter-num {
    margin-right: 6px;
    margin-bottom: 10px;
    font-size: 11px;
    border: 1px solid #999;
    padding: 6px 6px 6px 8px;
    color: #4e4e4e;
  }
  /* .ter-num s {
    position: relative;
    top: 3px;
    width: 13px;
    height: 13px;
    display: inline-block;
    margin-left: 15px;
    background: url(../assets/image/delete.png);
    cursor: pointer;
  } */
</style>


<style>
  /* 不加scoped自定义样式*利用类下类引用解决了全局污染 */
  .second-col .el-input {
    width: 319px;
  }
</style>
