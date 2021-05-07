import Vue from 'vue'
import Router from 'vue-router'

// 首页
import Home from '../pages/home'

// 用户信息
import UserNumber from '../pages/usernumber'
import UserNumberHome from '../components/usernumber/home'

Vue.use(Router)



export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/usernumber'
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
        }
      ]
    }
  ]
})
