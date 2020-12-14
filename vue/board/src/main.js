import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
