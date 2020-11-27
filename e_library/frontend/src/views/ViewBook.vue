<template>
    <v-container>
        <v-row>
            <v-col cols="12" md="4">
                <h1 class="pink--text">Views</h1>
            </v-col>
            <v-spacer></v-spacer>
            <v-col cols="12" md="4">
                <v-text-field
                    hide-details
                    prepend-icon="mdi-magnify"
                    single-line
                    v-model="search"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" md="4" v-for="book in books(search)" :key="book.id">
                <v-card>
                    <v-card-title>{{ book.title }}</v-card-title>
                    <v-card-subtitle>{{ book.id }}</v-card-subtitle>
                    <v-card-text>{{ book.body }}</v-card-text>
                </v-card>
            </v-col>
        </v-row>  
    </v-container>
</template>

<script>

export default {
    name: "ViewBook",
    data(){
        return {
            search: '',
        }
    },
    created(){
        this.$store.dispatch('getBook')
    },
    computed:{
        books(q){
            return this.$store.getters.getBooks({q})
        }
    }
}
</script>