Start();
function Start() {
	const vuetify = new Vuetify({
		theme: {
			dark: localStorage.getItem('library_dark'),
			options: {
				themeCache: {
					get(){return localStorage.getItem('library_dark')},
					set(){
						return localStorage.setItem('library_dark', !localStorage.getItem('library_dark') || false)
					},
				},
			}
		},
		icons: {
			iconfont: "md",
		},
	});

	new Vue({
		el: "#app",
		delimiters: ["${", "}"],
		data: () => ({
			drawer: false,
			name: "Test Name Vue",
		}),
		vuetify,
	});
}

