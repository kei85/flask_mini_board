import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state: {
    login_user: 0
  },
  mutations: {
    change_user(state, data) {
      state.login_user = data;
    }
  }
})