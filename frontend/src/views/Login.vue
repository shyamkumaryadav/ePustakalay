<template>
  <form @submit.prevent="submitForm">
      <h1>Login Form</h1>
      <a href="/api/">API</a>
      <p>csrf : {{'csrftoken'}}</p>
      <v-text-field :label="username.label" @input="username.errors = null" filled type="text" name="username" v-model="username.value" required :error-messages="username.errors" ></v-text-field>
      <v-text-field :label="password.label" @input="password.errors = null" filled name="password" autocomplete="username" v-model="password.value" required :error-messages="password.errors" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :type="show1 ? 'text' : 'password'" @click:append="show1 = !show1" ></v-text-field>
      <v-btn type="submit" id="asas" name="login">Login</v-btn>
      <p>{{ info }}</p>
  </form>
</template>

<script>
export default {
    name: 'Login',
    data(){
        return ({
            username: {
                value: '',
                label: "Username",
                errors: []
            },
            password: {
                value: '',
                label: "Password",
                errors: []
            },
            show1: false,
            info: ''

        })
    },
    methods:{
        submitForm(){
            // console.log("lol ***************************************")
            const data = {username: this.username.value, password: this.password.value}
            this.password.value = ""
            this.$store.dispatch('users/login', data)
        }
    },
}
</script>

<style>

</style>