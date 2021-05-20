import Vue from 'vue'
import Router from 'vue-router'

// 首页
import Home from '../pages/home'

// 用户身份信息
import UserNumber from '../pages/usernumber'
import UserNumberHome from '../components/usernumber/home'

// 用户手机信息
import UserMobile from '../pages/usermobile'
import UserMobileHome from '../components/usermobile/home'

// 用户基本信息
import UserBasic from '../pages/userbasic'
import UserBasicHome from '../components/userbasic/home'

// 登陆
import Login from '../pages/login'

Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/usernumber'
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/',
      name: 'home',
      component: Home,
      redirect: '/usernumber',
      children: [
        {
          path: 'usernumber',
          name: 'usernumber',
          component: UserNumber,
          redirect: '/usernumber/home',
          children: [
            {
              path: 'home',
              name: 'usernumberhome',
              component: UserNumberHome
            }
          ]
        },
        {
          path: 'usermobile',
          name: 'usermobile',
          component: UserMobile,
          redirect: '/usermobile/home',
          children: [
            {
              path: 'home',
              name: 'usermobilehome',
              component: UserMobileHome
            }
          ]
        },
        {
          path: 'userbasic',
          name: 'userbasic',
          component: UserBasic,
          redirect: '/userbasic/home',
          children: [
            {
              path: 'home',
              name: 'userbasichome',
              component: UserBasicHome
            }
          ]
        }
      ]
    }
  ]
})
