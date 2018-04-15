
<template>
    <div class="kanban-base">
        <pipe-line :pipeLine="pipeLine" v-for="(pipeLine, index) in pipeLineList"></pipe-line>
    </div>
</template>

<script>
    import PipeLine from './components/PipeLine.vue';
    import Vue from 'vue';

    export default {
        name: 'app',
        components: {
            PipeLine,
        },
        data() {
            return {
            }
        },
        computed: {
            pipeLineList(){
                console.log(this.$store.state.pipeLineList);
                return this.$store.state.pipeLineList;
            },
        },
        methods: {
        }
    }
</script>
<style scoped>
    .kanban-base {
        display: flex;
    }
    
    
</style>