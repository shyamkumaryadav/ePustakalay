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
        console.log(data)
        console.assert(data.results.length > 0, "No Book Avalable")
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
