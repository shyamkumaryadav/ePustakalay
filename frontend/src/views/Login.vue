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
import auth from '../services/auth.service'

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
            console.log("lol ***************************************")
            auth.login(this.username, this.password)
            .then(res => console.log(res))
            .catch(error => console.error(error.response.data))

        }
    },
}
</script>

<style>

</style>