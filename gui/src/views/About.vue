<template>
  <div class="about">
    <h1>This is an about page as</h1>
    <router-link to="/Http404">Page not find</router-link>
  </div>
</template>

<script>
export default {
  created(){
    document.title = "About"
  }
}
</script>
