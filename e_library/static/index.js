new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: {
        test: "Hello shyam",
        theme: false
    },
    created: function(){
        console.log(this.$vuetify.theme.dark)
    },
    updated:function(){
      console.log("Update: ", this.$vuetify.theme.dark)
    }
  })