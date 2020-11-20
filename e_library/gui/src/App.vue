<template>
<div>
  <img alt="Vue logo" :src="`${staticurl}gui/img/logo.png`">
  <h1>{{ count }}</h1>
  <HelloWorld :msg="staticurl"/>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  computed:{
    staticurl: () => document.body.dataset.staticUrl,
    count: this.$store.state.count
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
