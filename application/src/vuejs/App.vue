
<template>
    <div class="kanban-base">
        <pipe-line :pipeLine="pipeLine" v-for="(pipeLine, index) in pipeLineList"></pipe-line>
        <button class="add-button" @click="addPipeLine">ADD</button>
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
            addPipeLine(e){
                let title = window.prompt('title');
                if(title === undefined || title === null){
                    return;
                }
                this.$store.dispatch('add_pipeline', {
                    'kanbanId': 1,
                    'title': title,
                    'order': this.pipeLineList.length,
                });
            }
        }
    }
</script>
<style scoped>
    .kanban-base {
        display: flex;
    }
    .add-button {
        font-size: 1.2em;
        height: 40px;
        border: solid;
        padding: 5px;
        margin: 5px;
        width: 100px;
        cursor: pointer;
    }
    .add-button:hover {
        background-color: #333333;
        color: #fffccf;
    }

    
    
</style>