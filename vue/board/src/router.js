import Vue from 'vue'
import Router from 'vue-router'

import Login from './components/Login'
import Regist from './components/Regist'
import Home from './components/Home'
import MyIndex from './components/MyIndex'
import BoardAdd from './components/BoardAdd'

import store from './store'

Vue.use(Router)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      isPublic: true
    }
  },
  {
    path: '/regist',
    name: 'regist',
    component: Regist,
    meta: {
      isPublic: true
    }
  },
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      isPublic: true
    }
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

const router = new Router({
  mode: 'history',
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(page => page.meta.isPublic || store.state.login_user.state)) {
    next();
  } else {
    next('/login');
  }
});

export default router;