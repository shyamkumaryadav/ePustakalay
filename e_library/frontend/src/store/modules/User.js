export default {
    // namespaced: true,
    state: {
        username: '',
        is_login: false,
        is_active: false,
        is_superuser: false,
        refresh: sessionStorage.getItem('user_refresh') ?? '' ,
        access: sessionStorage.getItem('user_access') ?? '',

    },
    // Mutat the state (Update state) commit
    mutations: {
        getUser(state, payload){
            // console.log("Mutat user Data: ", payload)
            state.refresh = payload.refresh
            state.access = payload.access
            sessionStorage.setItem('user_refresh', payload.refresh)
            sessionStorage.setItem('user_access', payload.access)
        },
        updateLogin(state, payload){
            state.is_login = Object.entries(payload).length == 0
        }

    },
    // Called from components to commit a mutation (like api call) dispatch
    actions: {
        async login({commit}, {url, username, password}){
            const data = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                cache: "no-cache",
                body: JSON.stringify({username, password})
            })
            const user = await data.json();
            commit('getUser', user)
        },
        checkLogin({commit}, {url, access}){
            fetch(url, {
                method: "POST",
                headers:{
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({token: access})
            })
            .then(res => res.json())
            .then(data => commit('updateLogin', data))
            .catch(error => console.log("Error: ", error))
        }

    },
    getters:{
        get_username: (state) => state.username,
        is_authenticated: (state) => state.is_active
    },
  }