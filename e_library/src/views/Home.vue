<template>
  <div class="home">
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae quae voluptas explicabo quaerat culpa consectetur qui eveniet dolorem itaque saepe nostrum, magni quod voluptatibus ipsum maxime tenetur, exercitationem eos laborum.</p>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
