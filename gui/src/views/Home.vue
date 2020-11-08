<template>
  <v-col>
    <router-link to="/Http404">{{ $store.state.isDark }}</router-link>
    <h1>{{ $route.path }} </h1>
    <v-switch v-model="$store.state.isDark"></v-switch>
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

export default {
  name: 'Home',
  created(){
    document.title = "Home"
    console.log("Working");
    console.log(this.$store.state.isDark);
  }
}
</script>
