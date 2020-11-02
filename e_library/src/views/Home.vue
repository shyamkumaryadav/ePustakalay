<template>
  <div class="home">
    <h1>This is Home</h1>
    <div>
      <ol v-for="b in book" :key="b.id">
          <li>
            {{ b.first_name }} {{ b.last_name }}
          </li>
      </ol>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data() {
    book: [],
    messag: "Api work proper"
  },
  created:function(){
    console.log("Created Home API")
    fetch('/system/Books/').then(
      res => console.log(res.data)
    ).then(
      data => book = data
    ).catch(
      err => console.error('Error: ',err)
    )
  }
}
</script>
