import { URL, API} from '@/services/http-common.js'

export default {
    namespaced: true,
    state: {
      books: {},
      bookAuthors: {},
      bookPublish: {},
      bookGenres: {},
      bookIssue: {}
    },
    actions: {
      getBooks({dispatch}){
        API.get(URL.books)
        .then(response => {
          dispatch("setData", {name: 'books', value: response.data})
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      },
      getAuthors({dispatch}){
        API.get(URL.books)
        .then(response => {
          dispatch("setData", {name: 'books', value: response.data})
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      },
      
    },
    mutations: {
      setData(state, payload){
        state[payload.name] = payload.value
      }
    },
    getters: {},
  }