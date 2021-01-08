<template>
  <v-container fluid>

    <v-row>
      <v-img contain src="https://raw.githubusercontent.com/shyamkumaryadav/E_library/master/src/system/static/system/images/imgs/in-homepage-banner.jpg">
        <template v-slot:placeholder>
          <v-skeleton-loader
          type="image"
          class="fill-height ma-0"
          align="center"
          justify="center"
          ></v-skeleton-loader>
      </template>
      </v-img>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" class="text-center text--secondary">
        <h2>Our Features</h2>
        <p><b>Our 3 Primary Features -</b></p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="i in Features" :key="i.id" align="center">
          <v-img
            width="125px"
            :src="`https://raw.githubusercontent.com/shyamkumaryadav/E_library/master/src/system/static/system/images/imgs/${i.img}`"
          >
            <template v-slot:placeholder>
              <v-skeleton-loader
              type="image"
              class="fill-height ma-0"
              ></v-skeleton-loader>
            </template>
          </v-img>
          <v-card-title class="justify-center">{{i.title}}</v-card-title>
          <v-card-text class="text-center">
            {{ i.body }}
          </v-card-text>
      </v-col>
    </v-row>

    <v-row>
      <v-img contain src="https://raw.githubusercontent.com/shyamkumaryadav/E_library/master/src/system/static/system/images/imgs/in-homepage-banner.jpg">
        <template v-slot:placeholder>
          <v-skeleton-loader
          type="image"
          class="fill-height ma-0"
          ></v-skeleton-loader>
      </template>
      </v-img>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" class="text-center text--secondary">
        <h2>Our Process</h2>
        <p><b>We have a Simple 3 Step Process</b></p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="i in Process" :key="i.id" align="center">
          <v-img
            width="125px"
            :src="`https://raw.githubusercontent.com/shyamkumaryadav/E_library/master/src/system/static/system/images/imgs/${i.img}`"
          >
            <template v-slot:placeholder>
              <v-skeleton-loader
              type="image"
              class="fill-height ma-0"
              ></v-skeleton-loader>
            </template>
          </v-img>
          <v-card-title class="justify-center">{{i.title}}</v-card-title>
          <v-card-text class="text-center">
            {{ i.body }}
          </v-card-text>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
// @ is an alias to /src
// import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  data(){
    return {
      Features: [
        {
          id:1,
          img: 'digital-inventory.png',
          title: 'Digital Book Inventory',
          body: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        },
        {
          id:2,
          img: 'search-online.png',
          title: 'Search Books',
          body: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        },
        {
          id:3,
          img: 'defaulters-list.png',
          title: 'Defaulter List',
          body: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }
      ],
      Process:[
        {
          id:1,
          img: 'sign-up.png',
          title: 'Sign Up',
          body: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        },
        {
          id:2,
          img: 'search-online.png',
          title: 'Search Books',
          body: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        },
        {
          id:3,
          img: 'library.png',
          title: 'Visit Us',
          body: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }
      ]
    }
  }
}
</script>