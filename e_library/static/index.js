const vuetify = new Vuetify({
theme: {
dark: false,
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
name: "{{ user }}",
}),
vuetify,
});
