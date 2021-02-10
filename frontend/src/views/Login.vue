<template>
  <form @submit.prevent="submitForm">
      <h1>Login Form</h1>
      <a href="/api/">API</a>
      <p>csrf : {{'csrftoken'}}</p>
      <label for="username">Username:</label>
      <input type="text" name="username" v-model="username">
      <label for="password">password:</label>
      <input type="password" name="password" autocomplete="username" v-model="password">
      <button type="submit" id="asas" name="login">Login</button>
      <p>{{ info }}</p>
  </form>
</template>

<script>
// import AuthService from '@/services/auth.service';
import http from '@/services/http-common.js';

export default {
    name: 'Login',
    data(){
        return ({
            username: '',
            password: '',
            info: ''

        })
    },
    methods:{
        submitForm(){
            http.post('auth/token/', {
                username: this.username, password: this.password
            })
            .then(data => this.info = data)
            .catch(error => console.log(error))
        }
    },
}
</script>

<style>

</style>