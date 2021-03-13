import Vue from 'vue'
import Vuex from 'vuex'
import users from '@/store/modules/users.js'
import books from '@/store/modules/books.js'

Vue.use(Vuex)


// https://vuex.vuejs.org/#what-is-a-state-management-pattern
// errors.keys => https://v2.vuetifyjs.com/en/components/alerts/
export default new Vuex.Store({
  state: {
    errors: [

    ]
  },
  mutations: {
    errorPush(state, payload){
      state.errors.push(payload)
    },
    errorPop(state){
      state.errors.shift()
    }
  },
  actions: {
    setError({ commit }, payload ){
      commit('errorPush', payload)
      setTimeout(() => commit('errorPop'), payload.time)
    }
  },
  modules: {
    users,
    books
  }
})
