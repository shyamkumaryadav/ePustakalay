import Vue from 'vue'
import Vuex from 'vuex'
import theme from './modules/theme'

// Load Vuex
Vue.use(Vuex)

// create store
export default new Vuex.Store({
  // App level data/state
  state: {
  },
  // Mutat the state (Update state)
  mutations: {
  },
  // Called from components to commit a mutation (like api call)
  actions: {
  },
  // get Edit data ("iam".UPPERCASE > IAM)
  getters:{
  },
  // Each one have own state, getters, actions, mutations
  modules:{
    theme
  }
})
