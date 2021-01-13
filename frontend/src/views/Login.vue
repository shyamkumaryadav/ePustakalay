<template>
  <form @submit.prevent="submitForm">
      <h1>Login Form</h1>
      <p>csrf : {{scrf}}</p>
      <label for="username">Username:</label>
      <input type="text" name="username" v-model="username">
      <label for="password">password:</label>
      <input type="password" name="password" autocomplete="username" v-model="password">
      <button type="submit" id="asas" name="login">Login</button>
      <p>{{ info }}</p>
  </form>
</template>

<script>
import AuthService from '@/services/auth.service';

export default {
    name: 'Login',
    data(){
        return ({
            username: '',
            password: '',
            scrf: document.querySelector('[name=csrfmiddlewaretoken]').value,
            info: ''

        })
    },
    methods:{
        async submitForm(){
            this.info = await AuthService.login({username:this.username, password:this.password})
        }
    },
    watch:{
        username(newvalue){
            console.log('update username: ', newvalue)
        },
        password(newvalue){
            console.log('update password: ', newvalue)
        }
    }
}
</script>

<style>

</style>