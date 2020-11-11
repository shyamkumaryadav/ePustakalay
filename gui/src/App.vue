<template>
  <!-- <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div> -->
  <!-- <v-app-bar
  dense
  flat
><v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Page title</v-toolbar-title>

    </v-app-bar> -->
    <v-app id="inspire">
    <!-- <v-system-bar app>
      <v-spacer></v-spacer>
      <v-icon>mdi-wifi-strength-4</v-icon>
      <v-icon>mdi-signal-cellular-outline</v-icon>
      <v-icon>mdi-battery</v-icon>
      <span>12:30</span>
    </v-system-bar> -->

    <v-app-bar app hide-on-scroll>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title >E library</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn icon @click="$vuetify.theme.dark = !$vuetify.theme.dark">
        <v-icon>mdi-theme-light-dark</v-icon>
      </v-btn>

      <!-- <v-responsive max-width="156" class="hide-md">
        <v-text-field
          dense
          flat
          hide-details
          rounded
          solo-inverted
        ></v-text-field>
      </v-responsive> -->
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>status {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      fixed
      app
      temporary
    >
    <template v-slot:prepend>
        <v-list-item two-line>
          <v-list-item-avatar>
            <img src="https://randomuser.me/api/portraits/men/81.jpg">
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>Anonymous User</v-list-item-title>
            <v-list-item-subtitle>{{ isDark }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
      <v-divider></v-divider>
      <v-list
        nav
        dense
      >
        <v-list-item-group>
          <v-list-item :to="{path: '/'}">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{path: '/about'}">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block>
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-main>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import {mapState, mapMutations} from 'vuex'
export default {
  name: 'App',
  data: () => ({ drawer: null }),
  computed: {
   ...mapState(['isDark'])
  },
  methods:{
    ...mapMutations(['chanegTheme']),
    localTheme(){
      this.$store.state.commit('changeTheme') // store Dark mode
      // console.log(this);
    }
  }
}
</script>


