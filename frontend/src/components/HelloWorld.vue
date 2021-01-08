<template>
  <v-container>
    <v-row>
      <v-col>
        <v-img :src="require('@/assets/logo.svg')" min="150"></v-img>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col md="3" class="pa-6">
        Lorem ipsum dolor, sit shyam consectetur adipisicing elit. Non voluptatum commodi facilis corporis nostrum repudiandae quod dolores dolore libero cumque illo aperiam qui, perspiciatis similique shyam ipsum inventore culpa obcaecati.
      </v-col>
      <v-col md="3" class="pa-6">
        Lorem ipsum dolor, sit shyam consectetur adipisicing elit. Non voluptatum commodi facilis corporis nostrum repudiandae quod dolores dolore libero cumque illo aperiam qui, perspiciatis similique shyam ipsum inventore culpa obcaecati.
      </v-col>
      <v-col md="3" class="pa-6">
        Lorem ipsum dolor, sit shyam consectetur adipisicing elit. Non voluptatum commodi facilis corporis nostrum repudiandae quod dolores dolore libero cumque illo aperiam qui, perspiciatis similique shyam ipsum inventore culpa obcaecati.
      </v-col>
      <v-col md="3" class="pa-6">
        Lorem ipsum dolor, sit shyam consectetur adipisicing elit. Non voluptatum commodi facilis corporis nostrum repudiandae quod dolores dolore libero cumque illo aperiam qui, perspiciatis similique shyam ipsum inventore culpa obcaecati.
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',
    created(){
      document.title = "I am Home"
    },
    data: () => ({
      // lol
    }),
  }
</script>
