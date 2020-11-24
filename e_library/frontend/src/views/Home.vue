<template>
  <v-container fluid>
    <v-row>
      <v-img contain src="https://raw.githubusercontent.com/shyamkumaryadav/E_library/master/src/system/static/system/images/imgs/home-bg.jpg">
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
      <v-col cols="12" class="text-center subtitle-1 text--disabled">
        <h2>Our Features</h2>
        <p><b>Our 3 Primary Features -</b></p>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="4" class="text-center" v-for="i in [1, 2, 3]" :key="i">
        <img width="150px" src="https://raw.githubusercontent.com/shyamkumaryadav/E_library/master/src/system/static/system/images/imgs/digital-inventory.png"/>
        <h4>Digital Book Inventory</h4>
        <p class="align-middle">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </v-col>
    </v-row>
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
      <v-col cols="12" class="text-center subtitle-1 text--disabled">
        <h2>Our Process</h2>
        <p><b>We have a Simple 3 Step Process</b></p>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="4" class="text-center" v-for="i in [1, 2, 3]" :key="i">
        <img width="150px" src="https://raw.githubusercontent.com/shyamkumaryadav/E_library/master/src/system/static/system/images/imgs/digital-inventory.png"/>
        <h4>Digital Book Inventory</h4>
        <p class="align-middle">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
// import { mapGetters } from 'vuex'

export default {
  name: 'Home',
}
</script>
