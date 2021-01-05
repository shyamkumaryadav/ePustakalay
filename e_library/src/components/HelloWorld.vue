<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
       Hello world Comp
      </v-col>
      <img :src="require('@/assets/Images/404.png')" alt="" srcset="">
    </v-row>
  </v-container>
</template>

<script>

  export default {
    name: 'HelloWorld',

    data: () => ({
    //  data
    }),
  }
</script>
