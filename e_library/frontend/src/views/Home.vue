<template>
  <div class="home">
    <h1>Home Dark {{ isDark }}</h1>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  computed:mapGetters(['isDark'])
}
</script>
