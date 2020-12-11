import Vue from 'vue'
import Router from 'vue-router'

import Login from './components/Login'
import Regist from './components/Regist'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/users/login',
      name: 'login',
      component: Login
    },
    {
      path: '/users/regist',
      name: 'regist',
      component: Regist
    }
  ]
})