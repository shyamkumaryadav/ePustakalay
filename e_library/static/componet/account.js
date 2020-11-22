<script type="text/x-template" id="app-template">
    <v-app>
        <v-container>
        <h1>{{ count }} <i class="material-icons">face</i> </h1>            
        </v-container>
    </v-app>
</script>

Vue.component('app-render', {
	data: function () {
	  return {
		count: 0
	  }
	},
	template: '#app-template'
})