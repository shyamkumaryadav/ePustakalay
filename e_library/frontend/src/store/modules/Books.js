export default {
    // namespaced: true,
    state: {
        BooksList: [],
        isDone: true
    },
    // Mutat the state (Update state)
    mutations: {
        setBook(state, payload){
            state.BooksList = payload.books
            state.isDone = false
        }

    },
    // Called from components to commit a mutation (like api call)
    actions: {
        async getBook({commit}){
            const book = await fetch('https://jsonplaceholder.typicode.com/posts')
            const json = await book.json();
            console.log(json);
            commit('setBook', {
                books: json
            })

        }
    },
    getters:{
    },
  }