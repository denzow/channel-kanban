import App from './App.vue';
import Vue from 'vue';
import 'va/lib/css'
import 'va/lib/script'


new Vue({
    el: '#app',
    components: {
        App
    },
    template: '<app></app>'
});

Vue.component(App);