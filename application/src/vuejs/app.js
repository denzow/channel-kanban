import App from './App.vue';
import Vue from 'vue';
import Vuex from 'vuex';
import Store from './store/Kanban';

Vue.use(Vuex);


new Vue({
    store: new Vuex.Store(Store),
    el: '#app',
    components: {
        App
    },
    template: '<app></app>'
});

Vue.component(App);