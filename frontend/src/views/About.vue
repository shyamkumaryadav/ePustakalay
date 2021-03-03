<template>
  <div>
    <h1>This is an books</h1>
    <v-row v-for="book in books" :key="book.id">
      <p>{{ book.title}}</p>
    </v-row>
    <div>
      <v-btn v-show="books.previous" @click="getBooks(books.previous)"><span>previous</span></v-btn>
      <v-btn disabled v-show="books.count" >{{books.count}}</v-btn>
      <v-btn v-show="books.next" @click="getBooks(books.next)">Next</v-btn>
      <v-btn>Button</v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  data(){
    return ({
      books: {}
    })
  },
  created(){
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res => res.json())
      .then(data => {
        this.books = data
      })
      .catch(error => console.error(error))
  },
  methods:{
    getBooks(url){
      fetch(url)
      .then(res => res.json())
      .then(data => this.books = data)
    },
  },
  computed:{
    // computed
  }
}
</script>
