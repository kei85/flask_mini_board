import Vue from 'vue'
import Router from 'vue-router'

import Login from './components/Login'
import Regist from './components/Regist'
import Home from './components/Home'
import MyIndex from './components/MyIndex'
import BoardAdd from './components/BoardAdd'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/regist',
      name: 'regist',
      component: Regist
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/index/:id',
      name: 'myindex',
      component: MyIndex
    },
    {
      path: '/add/:id',
      name: 'add',
      component: BoardAdd
    }
  ]
})