import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    // dark = false
    breakpoint: {
      mobileBreakpoint: 'sm' // This is equivalent to a value of 960
    },
  },
});
