<template>
  <div class="about">
    <h1>This is an books</h1>
    <a href="/api/books/" target="_blank">list Books</a>
    <v-row v-for="book in books.results" :key="book.url">
      <v-col md=3>
        <v-img :src="book.profile" max-height="150" max-width="250"></v-img> {{ book.name }}
      </v-col> 
    </v-row>
    <div>
      <v-btn v-show="books.previous" @click="getBooks(books.previous)">{{ "<-" }}</v-btn>
      <v-btn disabled v-show="books.count" >{{books.count}}</v-btn>
      <v-btn v-show="books.next" @click="getBooks(books.next)">-></v-btn>
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
    fetch('/api/books/')
      .then(res => res.json())
      .then(data => {
        data.results.length > 0 ?  console.log("Book") : console.error("No Book Avalable")
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
