<template>
  <div>
      <v-btn @click="getUsers">Get Users</v-btn>
      <v-btn @click="getBlob">Load Image</v-btn>
      <p>{{ users }}</p>
      <v-img aspect-ratio="1.7" ref="UserImage"></v-img>
    </div>
</template>

<script>
import Api from '@/services/http-common.js'

export default {
    data(){
        return ({
            listValue: '',
            listData: [],
            snackbar: true,
            users: {},
        })
    },
    methods:{
        addMe(){
            this.listData.push({text:this.listValue, is_show:true})
            this.listValue = ''
        },
        getUsers(){
            Api('/user/')
            .then(res => this.users = res.data)
            .catch(error => console.log(error))
        },
        getBlob(){
            Api({
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