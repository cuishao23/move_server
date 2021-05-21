<template>
    <span class="bg">
        <div id="wrap" class="clearfix">
            <div id="login_header" class="clearfix">
                <div class="login_header_bg"></div>
            </div>
            <div class="content">
                <div class="login_content clearfix">
                    <div id="login_form">
                        <div class="clearfix form_input_holder">
                            <div class="login_input_wrapper">
                                <input type="text" class="login-input" id="username" v-model="username" maxlength="64" name="username"
                                       @focus="account_prompt=false" @blur="username!=''?false:account_prompt=true"/>
                                <label class="tip_label" v-show="account_prompt"
                                       @click="account_prompt=false" for="username">用户名</label>
                            </div>

                            <div class="login_input_wrapper password_input_holder">
                                <input type="password" class="login-input" id="passwd" v-model="passwd" maxlength="32" name="passwd"
                                       @focus="passwd_prompt=false" @blur="passwd!=''?false:passwd_prompt=true"
                                       @keyup.enter="submit"/>
                                <label class="tip_label" v-show="passwd_prompt" @click="passwd_prompt=false" for="passwd">密码</label>
                            </div>
                            <div class="error_msg" v-show="err_msg!==''">{{err_msg}}
                            </div>
                            <a id="login-submit" class="login" @click="submit()" @keyup.enter="submit">登录</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div style="height: 143px;"></div>
        <div class="enterprise_introduce_content clearfix" style="width:100%;">

            <div class="company_info_up ">
                <p class="clearfix company_info">
                    <a class="no_meeting_icon phone_icon"></a>
                    <span class="phone">021-55898033</span>
                    <a class="no_meeting_icon emal_icon"></a>
                    <span class="emal">info@moveclub.cn</span>
                    <a class="no_meeting_icon no_meeting"></a>
                    <span class="meeting"><a href="https://www.moveclub.cn/" target="_blank">www.moveclub.com</a></span>
                </p>
            </div>
            <div class="company_info_down" style="margin-top:10px;">
                <p class="clearfix company_info">
                    <span class="footVerInfo">每步科技(上海)有限公司</span>
                    <span class="footVerInfo left24" style="margin-left: 16px">Copyright &copy; 2015-<span
                        class="version_year">2021</span> MOVE. All rights reserved.</span>
                </p>
            </div>
        </div>
    </span>
</template>

<script>
    import api from '../axios'
    export default {
        name: "login",
        data() {
            return {
                username: '',
                passwd: '',
                image_code: '',
                image_code_url: '',
                err_msg: '',
                next: '',
                show_image: false,

                account_prompt: true,
                passwd_prompt: true,
                img_code_prompt: true,
                DEBUG: false,

                login_data: {}
            }
        },
        methods: {
            setCookie: function (cname, cvalue, exdays) {
                var d = new Date();
                d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
                var expires = "expires=" + d.toUTCString();
                document.cookie = cname + "=" + cvalue + "; " + expires;
              },
            async submit() {
                if (this.username === '') {
                    this.err_msg = '请输入用户名后提交';
                    return
                } else {
                    this.err_msg = ''
                }
                if (this.passwd === '') {
                    this.err_msg = '请输入密码后提交';
                    return
                } else {
                    this.err_msg = ''
                }
                
                this.login_data['username'] = this.username
                this.login_data['passwd'] = this.passwd
                api.postLoginInfo(this.login_data).then(res => {
                  if (res.success == 1) {
                      this.setCookie('username',res.username,1);
                      console.log(document.location.origin)
                      document.location = document.location.origin
                    //   this.$router.push({name: "usernumber"})
                  } else {
                      this.err_msg = "用户名/密码错误"
                  }
                })
                .catch((error) => {
                    console.log(error);
                    this.err_msg = "用户名/密码错误";
                })
            }
        },
    }
</script>

<style scoped>
    .bg {
        background: #FFFFFF;
        text-align: center;
        overflow: auto;
    }

    #wrap {
        padding: 0 0 0;
    }

    #login_header {
        position: relative;
    }

    #login_header .login_header_bg {
        width: 100%;
        height: 377px;
        background: url(../assets/image/newBg.png) no-repeat center;
    }

    .login_logo {
        position: absolute;
        height: 11px;
        width: 72px;
        left: 35px;
        top: 29px;
        background: url(../assets/image/icon.png) no-repeat;
    }
    #login_header .sys_logo {
        position: absolute;
        left: 50%;
        top: 161px;
    }

    .sys_logo .logo_text {
        margin-left: 136px;
        font-size: 24px;
        text-align: left;
        vertical-align: top;
        line-height: 24px;
        color: rgb(204, 204, 204);
    }

    .sys_logo .logo_englishtext {
        margin-left: 136px;
        margin-top: 10px;
        font-size: 14px;
        text-align: left;
        vertical-align: top;
        line-height: 14px;
        color: #333333;
        font-family: "Arial";
    }

    #wrap .content {
        margin: 0 auto;
        width: 960px;
    }

    #wrap .login_content {
        height: 222px;
    }

    .login_content #login_form {
        width: 198px;
        position: relative;
        margin: 0 auto;
        padding-top: 46px;
        height: 176px;
    }

    .login {
        background-color: #000;
        cursor: pointer;
        height: 31px;
        position: relative;
        width: 198px;
        line-height: 31px;
        text-align: center;
        display: inline-block;
        margin-top: 40px;
        color: #ffffff;
        font-size: 14px;
    }

    .login:hover {
        background-color: #fff;
        border: 1px solid #2e8cc1;
        color: #2e8cc1;
    }

    #login_form .error_msg {
        color: #d53a3a;
        width: 198px;
        text-align: center;
        padding: 0;
        position: absolute;
        font-size: 12px;
        /*bottom: 36px;*/
    }

    .error_msg {
        overflow: hidden;
    }

    .login_content .login-input {
        background: none repeat scroll 0 0 transparent;
        border: medium none;
        color: #606060;
        font-size: 14px;
        height: 28px;
        line-height: 28px;
        width: 198px;
        text-align: center;
        outline: none
    }

    .login_content .login_input_wrapper {
        border: medium none;
        height: 28px;
        overflow: hidden;
        position: relative;
        width: 198px;
        display: block;
        border-width: 0 0 1px 0;
        border-style: solid;
        border-color: #949799;
        margin: 0 auto;
    }

    .login_content #login_form .password_input_holder {
        margin-top: 15px;
    }

    .login_input_wrapper .tip_label {
        position: absolute;
        left: 0;
        bottom: 7px;
        color: #606060;
        cursor: text;
        width: 198px;
        text-align: center;
        line-height: 14px;
        font-size: 14px;
        font-family: "微软雅黑";
    }

    .content input[type="text"] {
        display: block;
        width: 198px;
        text-align: center;
        height: 28px;
        margin: 0;
    }

    .content input[type="password"] {
        display: block;
        height: 28px;
        width: 198px;
        text-align: center;
        border-bottom: 1px solid #949799;
    }

    .icon {
        background: url(../assets/image/icon.png) repeat scroll 0 0 transparent;
    }

    .company_info_up {
        font-size: 14px;
        font-family: '微软雅黑';
        color: #4e4e4e;
    }

    .company_info_down {
        margin-top: 10px;
        font-family: '微软雅黑';
        font-size: 12px;
        color: #606060;
    }

    .enterprise_introduce_content {
        width: 560px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
        color: #616060;
    }

    .enterprise_introduce_content h2 {
        font-size: 16px;
    }

    .enterprise_introduce_content .connect_info {
        margin-top: 30px;
    }

    .enterprise_introduce_content .company_info {
        /* margin-top:10px; */
        margin-bottom: 0px;
    }

    .enterprise_introduce_content .enterprise_descript {
        margin: 18px 0 18px;
    }

    .enterprise_introduce_content .enterprise_tel,
    .enterprise_introduce_content .enterprise_mail,
    .enterprise_introduce_content .enterprise_net {
        display: block;
        float: left;
        padding-left: 28px;
        position: relative;
        text-align: left;
    }

    .enterprise_introduce_content .enterprise_mail,
    .enterprise_introduce_content .enterprise_net {
        margin-left: 40px;
    }

    .enterprise_tel .icon,
    .enterprise_net .icon,
    .enterprise_mail .icon {
        width: 18px;
        height: 18px;
        display: block;
        position: absolute;
        left: 0;
        top: 0;
    }

    .enterprise_tel .icon {
        background-position: 0 -513px;
    }

    .enterprise_net .icon {
        background-position: -56px -513px;
    }

    .enterprise_mail .icon {
        background-position: -28px -513px;
    }

    .company_info span.phone,
    .company_info span.emal,
    .company_info .no_meeting,
    .company_info span.meeting a {
        vertical-align: top;
    }

    .no_meeting_icon {
        background: transparent url(../assets/image/icon.png) no-repeat scroll 0 0;
    }

    .phone_icon {
        background-position: -1px -513px;
        display: inline-block;
        height: 17px;
        margin-right: 10px;
        width: 16px;
    }

    .emal_icon {
        background-position: -28px -513px;
        display: inline-block;
        height: 17px;
        margin-right: 10px;
        margin-left: 43px;
        width: 18px;
    }

    .no_meeting {
        background-position: -54px -513px;
        display: inline-block;
        height: 22px;
        margin-right: 10px;
        margin-left: 43px;
        width: 19px;
    }

    .login_content #login_form .verifyCode_input_holder {
        width: 198px;
        border: 0px;
        text-align: left;
        height: 45px !important;
    }

    .verifyCode_input_holder .login-input {
        margin-top: 15px !important;
        width: 99px !important;
        border-bottom: 1px solid #949799;
        display: inline-block !important;
    }

    .verifyCode_input_holder .tip_label {
        width: 99px;
    }

    #verifyImage {
        margin-top: -10px;
        cursor: pointer;
        width: 92px;
        height: 25px;
        text-align: left;
    }

</style>
