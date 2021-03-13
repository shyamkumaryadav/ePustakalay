import { LOGIN, AUTHAPI, URL, ACCESS_TOKEN, LOGOUT } from '../../services/http-common'

export default {
    // store.commit('mutation') <=> store.commit('name/mutation')
    namespaced: true, // we can commit by name but if we have many mutation with same name it's hard to do so we use namespace
    state: {
        user: {},
        login: false
    },
    actions: {
        // { dispatch, commit, getters, rootGetters }, payload => async
        login({dispatch, commit}, payload){
            const {username, password} = payload
            LOGIN(username, password)
            .then(response => {
                console.log(response)
                dispatch('getUser').then(()=> commit('userLogin')).catch(() => commit('userLogout'))
            })
            .catch(error => dispatch('setError', {type: 'error', text: error.response.data.detail}, {root: true}))
        },
        getUser({commit}){
            AUTHAPI(URL.userList)
            .then(response => {
                console.log(response.data)
                commit('setUser', response.data)
            })
            .catch(error => console.log(error.response.data))
        },
        logout({dispatch}){
            LOGOUT()
            dispatch('userLogout')
        }
    },
    mutations: {
        setUser(state, payload){
            state.user = payload
        },
        userLogin(state){
            localStorage.getItem(ACCESS_TOKEN) ? state.login = true : null
        },
        userLogout(state){
            state.user = {}
            state.login = false
        }
    },
    // dispatch('someOtherAction', payload, { root: true }); 
    // commit('someMutation', payload, { root: true });
    getters: {
        // state, getters, rootState, rootGetters
        getUser(state){
            return state.user
        },
        is_login(state){
            return state.login
        },
        is_superuser(state){
            return state?.user?.
        }
    },
  }