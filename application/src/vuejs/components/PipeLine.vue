<template>
    <div class="pipeline">
        <div class="pipeline-title">{{pipeLine.name}}</div>

        <div class="card-list">
            <draggable>
                <card :card="card" v-for="(card, i) in pipeLine.cards"></card>
            </draggable>
        </div>
    </div>
</template>
<script>
    import Card from './Card.vue';
    import draggable from 'vuedraggable';

    export default {
        name: 'PipeLine',
        props: [
            'pipeLine'
        ],
        components: {
            Card,
            draggable,
        }
    }

</script>
<style scoped>
    .pipeline {
        margin: 5px;
        padding: 5px;
        width: 100px;
        border: solid;
    }
    .pipeline-title {
        text-align: center;
        padding: 5px;
        border: solid;
    }

</style>