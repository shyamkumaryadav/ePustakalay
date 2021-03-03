export default {
    // store.commit('mutation') => store.commit('name/mutation')
    namespaced: true, // we can commit by name but if we have many mutation it's hard to do so we use namespace
    state: {
        user: {},
    },
    // { dispatch, commit, getters, rootGetters }, payload
    actions: {},
    mutations: {},
    // state, getters, rootState, rootGetters
    // dispatch('someOtherAction', payload, { root: true }); 
    // commit('someMutation', payload, { root: true });
    getters: {},
  }