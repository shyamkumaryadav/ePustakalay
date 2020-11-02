<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <router-link to="/">
        <div class="d-flex align-center">
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
            transition="scale-transition"
            width="40"
          />

          <v-text>Home</v-text>
        </div>
      </router-link>

      <v-spacer></v-spacer>

      
      <router-link to="/about">
        <v-btn
        text
        >
          <span class="mr-2">About</span>
          <v-icon>open_in_new</v-icon>
        </v-btn>
      </router-link>
        
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
