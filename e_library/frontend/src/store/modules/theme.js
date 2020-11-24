export default {
    // namespaced: true,
    state: {
      dark: true
    },
    // Mutat the state (Update state)
    mutations: {
        setDark: state=> {
            state.dark = !state.dark
            localStorage.setItem('elibrary-theme', state.dark)
        }
    },
    // Called from components to commit a mutation (like api call)
    actions: {
        changeTheme({commit}){
            commit('setDark')
        }
    },
    getters:{
        isDark: state => state.dark
    },
  }