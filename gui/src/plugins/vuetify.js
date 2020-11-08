import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import store from '@/store/index.js'


Vue.use(Vuetify);

export default new Vuetify({
    theme:{
        dark: store.state.isDark,
    }
});
