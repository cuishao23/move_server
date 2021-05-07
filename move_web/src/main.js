import 'babel-polyfill'
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import Element from 'element-ui';

// import $ from 'jquery'

import axios from './axios/api';
import './assets/css/common.css';
import './assets/css/messagebox.css';
import './assets/css/reset.css';
// import 'animate.css';

require('es6-promise').polyfill();
Vue.prototype.axios = axios;
Vue.use(Element);
Vue.prototype.app = App;
Vue.config.productionTip = false;

// Mock.init();
router.beforeEach((to, from, next) => {
  if (to.matched.length ===0) {                                 //如果未匹配到路由
      from.name ? next({ name:from.name }) : next('/');   //如果上级也未匹配到路由则跳转登录页面，如果上级能匹配到则转上级路由
  } else {
      next();                                                                            //如果匹配到正确跳转
  }
});
/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  axios,
  router
}).$mount('#app')
