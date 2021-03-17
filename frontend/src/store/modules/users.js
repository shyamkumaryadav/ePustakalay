import { LOGIN, AUTHAPI, URL, LOGOUT } from '../../services/http-common'

export default {
    // store.commit('mutation') <=> store.commit('name/mutation')
    namespaced: true, // we can commit by name but if we have many mutation with same name it's hard to do so we use namespace
    state: {
        user: {}
    },
    actions: {
        // { dispatch, commit, getters, rootGetters }, payload => async
        login({dispatch}, payload){
            const {username, password} = payload
            LOGIN(username, password)
            .then(response => {
                response === 'OK' ? dispatch('getUsers') : dispatch('logout')
            })
            .catch(error => dispatch('setError', {type: 'error', text: error.response.data.detail}, {root: true}))
        },
        logout({dispatch}){
            LOGOUT()
            dispatch('userLogout')
        },
        getUsers({commit}){
            AUTHAPI(URL.userList)
            .then(response => {
                if(response.data.count > 0){
                    commit('getUser', response.data)
                }else commit('setUser', response.data)
            })
            .catch(error => console.log(error.response.data))
        },
        getUser({commit}, payload){
            AUTHAPI(URL.userDetail.format(payload.id))
            .then(response => {
                commit('setUser', response.data)
            })
            .catch(error => console.log(error.response.data))
        },
    },
    mutations: {
        setUser(state, payload){
            state.user = payload
        },
       
        userLogout(state){
            state = {}
        }
    },
    // dispatch('someOtherAction', payload, { root: true }); 
    // commit('someMutation', payload, { root: true });
    getters: {
        // state, getters, rootState, rootGetters
        getUsers(state){
            return state.user
        },
        is_login(state){
            return state?.user?.username
        },
        is_superuser(state){
            return state?.user?.is_superuser
        }
    },
  }