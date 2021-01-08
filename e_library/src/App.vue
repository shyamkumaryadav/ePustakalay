<template>
  <div id="app">
    <h1>Master Page</h1>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quidem repudiandae est ducimus reprehenderit possimus nostrum ea quod iure magni, ratione minima? Commodi ex voluptatem at veniam hic animi tempore odio!</p>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  created(){
    console.log("lol xD")
  },

}
</script>

<style>

</style>