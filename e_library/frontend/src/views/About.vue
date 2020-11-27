<template>
  <v-container>
      <v-row>
          <v-col cols="12" md="4">
              <h1>Login {{ $store.state.User.is_login }}</h1>
          </v-col>
      </v-row>
      <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="username"
              label="Name"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="password"
              label="Password"
              :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show ? 'text' : 'password'"
              @click:append="show = !show"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-btn
              large
              outlined
              text
              @click="login"
            >Login</v-btn>
          </v-col>
      </v-row>  
    </v-container>
</template>

<script>
// import { router } from 'vue-router'

export default {
  name: "About",
  data(){
    return {
      show: false,
      username: '',
      password: ''
    }
  },
  created(){
    const url = "http://127.0.0.1:8000/api/auth/token/verify/"
    this.$store.dispatch('checkLogin', {url, access:sessionStorage.getItem('user_access')})
    this.$store.state.User.is_login ? this.$router.push({ name: 'Home'}) : null
  },
  updated(){
    // 
  },
  methods:{
    login(){
      if (this.username && this.password){
        const url = "http://127.0.0.1:8000/api/auth/token/"
        this.$store.dispatch('login', {url, username: this.username, password: this.password})
      }
    }


  }
}
</script>
