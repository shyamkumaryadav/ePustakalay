import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isDark: false,
  },
  mutations: {
    chanegTheme(state){
      state.isDark = !state.isDark
    }
  },
  actions: {
    themeChange({commit}){
      commit('changeTheme')
    }
  },
  getters:{
    theme(state){
      return state.isdark
    }
  },
  modules: {
  }
})
