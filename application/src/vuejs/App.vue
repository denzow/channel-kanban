
<template>
    <div class="kanban-base">
        <pipe-line :pipeLine="pipeLine" v-for="(pipeLine, index) in pipeLineList"></pipe-line>
    </div>
</template>

<script>
    import PipeLine from './components/PipeLine.vue';

    export default {
        name: 'app',
        components: {
            PipeLine,
        },
        data() {
            return {
                pipeLineList: [
                    {
                        name: '1st',
                        cards: [
                            'a',
                            'b',
                            'c'
                        ]
                    },
                    {
                        name: '2nd',
                        cards: [
                            'd',
                            'e',
                        ]
                    }
                ],
            }
        }
    }
</script>
<style scoped>
    .kanban-base {
        display: flex;
    }
    
    
</style>