<template>
  <div class="about">
    <h1>This is an books</h1>
    <p>{{ books }}</p>
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
        data.results.length > 0 ?  console.log("book ") : console.error("No Book Avalable")
        this.books = data
      })
      .catch(error => console.error(error))
  },
  methods:{
    // methos
  },
  computed:{
    // computed
  }
}
</script>
