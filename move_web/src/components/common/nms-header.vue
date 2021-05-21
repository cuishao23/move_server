<template>
  <el-row type="flex" class="nms-header" justify="space-around">
    <el-col :span="6" class="logo-parent">
      <div class="logo">
        <div><img src="../../assets/image/move.png" width="113px" height="35px"/></div>
        <div><img src="../../assets/image/header_cutline.png"><span id="fontTitle">数字营销数据平台</span></div>
      </div>
    </el-col>
    <el-col :span="6">
      <div class="grid-content bg-purple-light"></div>
    </el-col>
    <el-col :span="6" class="user-info">
      <div class="user-header"><img src="../../assets/image/user_header.png"/></div>
      <span id="userInfo">{{ user }}</span>
      <el-dropdown trigger="click" placement="bottom-end">
        <span class="el-dropdown-link nms-set"/>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item><a id="help" @click="help()">帮助信息</a></el-dropdown-item>
          <el-dropdown-item><a id="about" @click="about()">关于</a></el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <a id="exit" @click="logout()"></a>
      <nms-dialog title="提示" ref="logout" width="300px" height="200px" :confirmBtn="true" :closeBtn="true" @confirm="confirmLogout" @cancel="cancelLogout">
        <div slot="content" class="tbl-dlg">
          <p class="note-content">确认退出系统?</p>
        </div>
      </nms-dialog>
      <nms-dialog title="关于" ref="about" width="400px" height="300px" :confirmBtn="false" :closeBtn="false" >
        <div slot="content" class="tbl-dlg">
          <div class="about-container" v-if="brand == 1">
            <div class="about-item-container">
              <p class="about-item">每步科技(上海)有限公司 版权所有</p>
              <p class="about-item">Copyright © 2015-{{year}} MOVE. All Rights Reserved.</p>
              <div class="about-item">
                Version:{{version}}
                <span style="margin-left: 20px;"><a class="about-url" href="https://www.moveclub.cn">www.moveclub.cn</a></span>
              </div>
            </div>
          </div>
        </div>
      </nms-dialog>
    </el-col>
  </el-row>
</template>

<script>
  import ElRow from 'element-ui/packages/row/src/row'
  import NmsDialog from '../../components/common/nms-dialog'
  import api from '../../axios'
  export default {
    components: {ElRow, NmsDialog},
    name: 'nms-header',
    data() {
      return {
        brand: 1,
        version: '1.0.0',
        year: 2000,
        user: '未登陆用户'
      }
    },
    mounted: function() {
      if (this.getCookie('username')) {
        this.user = this.getCookie('username')
      }
      let date = new Date()
      this.year = date.getFullYear()
    },
    methods: {
      help: function () {
        console.log('帮助信息')
      },
      about: function() {
        this.$refs.about.open()
      },
      logout: function() {
        this.$refs.logout.open()
      },
      confirmLogout: function () {
        api.postLoginOutInfo().then(res => {
          if (res.success == 1) {
              this.$router.push({name: "login"})
              // 清除cookie
              this.setCookie("username", "", -1)
          }
        })
        .catch((error) => {
            console.log(error);
        })
        console.log('logout')
        console.log(window.location)
        // 跳转到登录页
        window.location = '/login'
        // this.$refs.logout.close()
      },
      cancelLogout: function () {
        console.log('cancel logout')
        this.$refs.logout.close()
      },
      //获取cookie
      getCookie: function (cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) == ' ') c = c.substring(1);
          if (c.indexOf(name) != -1){
            return c.substring(name.length, c.length);
          }
        }
        return "";
      },
      // 设置cookie
      setCookie: function (cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + "; " + expires;
      }
    }
  }
</script>

<style scoped>
  .logo-parent {
    display: flex;
    display: -webkit-flex;
    justify-content: center;
  }

  .logo {
    display: flex;
    justify-content: center;
  }

  .logo div, .logo span {
    padding: 0px 10px 0px 0px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .user-header {
    display: flex;
    align-items: center;
  }

  .nms-header {
    width: 100vw;
    min-width: 720px;
    height: 98px;
    background-color: #373d41;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
  }

  .nms-header #fontTitle {
    float: left;
    color: #fff;
    margin-left: 10px;
    font: bold 13px/13px Microsoft YaHei;
  }

  .nms-header #exit {
    width: 24px;
    height: 24px;
    margin: 37px 128px 0 0;
    background: url('../../assets/image/exit_all.png');
  }

  .nms-header #exit:hover {
    background: url('../../assets/image/exit_all.png') -24px 0px;
  }

  .el-dropdown {
    height: 68px;
  }

  .popper__arrow {
    display: none;
  }

  .nms-set {
    display: flex;
    align-items: baseline;
    width: 24px;
    height: 24px;
    margin: 37px 10px 0 0;
    background: url('../../assets/image/set_info.png');
  }

  .el-dropdown-menu, .el-dropdown-menu__item {
    background: none repeat scroll 0% 0% #FFF;
    /*border: 2px solid #E5E5E5;*/
    color: #333;
  }

  .el-dropdown-menu__item a {
    color: #4E4E4E;
    font-size: 12px;
    text-decoration: none;
    display: block;
    height: 100%;
  }

  .el-dropdown-menu__item {
    line-height: 34px;
    width: 112px;
    text-align: center;
    padding: 0px 0px 0px 0px;
  }

  .el-dropdown-menu__item a:hover, .el-dropdown-menu__item:hover, .el-dropdown-menu__item:hover a{
    background: none repeat scroll 0% 0% #46AAE4;
    color: #FFF;
  }

  .nms-set:hover {
    background: url('../../assets/image/set_info.png') -24px 0px;
  }

  .nms-header #userInfo {
    height: 12px;
    margin: 43px 18px 0 0;
    color: #fff;
    font: 12px/12px Microsoft YaHei;
  }

  .user-info {
    display: flex;
    justify-content: flex-end;
  }

  a:link {
    cursor: pointer;
  }

  .tbl-dlg {
    text-align: center;
    width: 100%;
    height: 100%;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
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

  .about-container {
    text-align: left;
    position: relative;
  }

  .about-title {
    font-size: 14px;
    font-weight: bold;
    color: #4e4e4e;
    position: absolute;
    top: 60px;
    right: 30px;
  }

  .about-item-container {
    margin-top: 55px;
  }

  .about-item {
    margin-top: 9px;
    font-size: 12px;
    color: #4e4e4e;
  }

  .about-url {
    font-size: 12px;
    color: #007ac0 !important;
    text-decoration: underline !important;
    margin-right: 17px;
  }
</style>
