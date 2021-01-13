<template>
  <div>
      <h1>Terms page</h1>
        <input type="text" v-model="listValue">
        <button @click="addMe">Add Data</button>
        <ul v-for="li in listData" :key="li">
            <li>{{ li }}</li>
        </ul>
        <v-snackbar v-for="li in listData" :key="li.text"
            v-model="li.text"
            timeout=12000
            >
            {{li.text}}
            <template v-slot:action="{ attrs }">
                <v-btn
                color="blue"
                text
                v-bind="attrs"
                @click="li.is_show = false"
                >
                Close
                </v-btn>
            </template>
            </v-snackbar>
    </div>
</template>

<script>
export default {
    data(){
        return ({
            listValue: '',
            listData: [],
            snackbar: true,
        })
    },
    methods:{
        addMe(){
            this.listData.push({text:this.listValue, is_show:true})
            this.listValue = ''
        }
    }
}
</script>

<style>

</style>