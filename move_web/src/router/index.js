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
import Bi from '../pages/bi'
import BiHome from '../components/bi/home'

// bi报表
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
        },
        {
          path: 'bi',
          name: 'bi',
          component: Bi,
          redirect: '/bi/home',
          children: [
            {
              path: 'home',
              name: 'bihome',
              component: BiHome
            }
          ]
        }
      ]
    }
  ]
})

// 解决路由重复报错
const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}
