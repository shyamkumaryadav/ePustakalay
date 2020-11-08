<template>
  <v-col>
    <!-- <router-link to="/Http404">hay ! {{ theme }}</router-link> -->
    <h1>{{ $route.path }} </h1>
    <!-- <v-switch v-model="theme"></v-switch> -->
    <img alt="Vue logo" src="@/assets/logo.png">
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, laudantium. Aliquid, animi, excepturi ipsa optio id nobis quam suscipit nostrum nisi temporibus, at sint illo delectus dolore qui nihil ea.</p>
    
  </v-col>
</template>

<script>
// @ is an alias to /src
import {mapGetters} from 'vuex'

export default {
  name: 'Home',
  created(){
    document.title = "Home"
  },
  computed:{
    ...mapGetters(['theme'])
  }
}
</script>
