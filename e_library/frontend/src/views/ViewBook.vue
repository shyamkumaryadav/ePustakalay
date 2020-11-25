<template>
<v-container fluid>
    <v-row>
      <v-col lg="4" md="1" sm="12" class="text-center" v-for="book in $store.state.Books.BooksList" :key="book.id">
        <v-card outlined>
            <v-card-title class="headline">
                {{ book.title}}
            </v-card-title>

            <v-card-subtitle>{{ book.body }}</v-card-subtitle>

            <v-card-actions>
            <v-btn text>
                Listen Now on {{ book.id }}
            </v-btn>
            </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import { mapActions } from 'vuex'

export default {
    name: "ViewBook",
    data: () => ({
        name: 'View books'
    }),
    created:function(){
        this.$store.dispatch('getBook')
    }
    
}
</script>