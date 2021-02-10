<template>
  <div>
      <form @submit.prevent="createUser" method="post">
          <input type="text" placeholder="username" v-model="username">
          <span v-for="msg in info.username" :key="msg">{{ msg }}</span><br>
          <input type="email" placeholder="email" v-model="email">
          <span v-for="msg in info.email" :key="msg">{{ msg }}</span><br>
          <input type="password" placeholder="password" v-model="password">
          <span v-for="msg in info.password" :key="msg">{{ msg }}</span><br>
          <input type="password" placeholder="confirm_password" v-model="confirm_password">
          <span v-for="msg in info.confirm_password" :key="msg">{{ msg }}</span><br>
          <v-btn type="submit">CreateUser</v-btn>
          <p>Login INFO: {{ info }}</p>
      </form>
      <v-btn @click="getUsers">Get Users</v-btn>
      <v-btn @click="getBlob">Load Image</v-btn>
      <p>{{ users }}</p>
      <v-img aspect-ratio="1.7" ref="UserImage"></v-img>
    </div>
</template>

<script>
import http from '@/services/http-common.js'

export default {
    data(){
        return ({
            listValue: '',
            listData: [],
            snackbar: true,
            users: {},
            username: '',
            email: '',
            password: '',
            confirm_password: '',
            info: 'Loading...',
        })
    },
    methods:{
        createUser(){
            http.post('user/create_user/', {
                username: this.username,
                email: this.email,
                password: this.password,
                confirm_password: this.confirm_password
            }).then(res => this.info = res.data)
            .catch(error => this.info = error.response.data)
        },
        addMe(){
            this.listData.push({text:this.listValue, is_show:true})
            this.listValue = ''
        },
        getUsers(){
            http('/user/')
            .then(res => this.users = res.data)
            .catch(error => console.log(error))
        },
        getBlob(){
            http({
                method: 'GET',
                url: 'http://localhost:8000/media/user.png',
                responseType: 'blob'
            }).then(res => {
                const new_blob = new Blob( [ res.data ], { type: 'image/png' } )
                const url = URL.createObjectURL( new_blob )
                this.$refs.UserImage.src = url
                this.users = res.data}
            ).catch(error => console.log(error))
        }
    }
}
</script>

<style>

</style>