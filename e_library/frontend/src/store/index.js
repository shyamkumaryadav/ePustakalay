import Vue from 'vue'
import Vuex from 'vuex'

// Load Vuex
Vue.use(Vuex)

// create store
export default new Vuex.Store({
  // App level data/state
  state: {
  },
  // The only way to actually change state in a Vuex store is by committing a mutation.
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
  }
})
