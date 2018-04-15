<template>
    <div class="pipeline">
        <div class="pipeline-title">{{pipeLine.name}} {{pipeLine.cards.length}}</div>
        <div class="card-list">
            <draggable @start="onStart" @end="onEnd" :options="options" v-model="cards">
                <card :card="card" v-for="(card, i) in cards"></card>
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
        },
        methods: {
            onStart: function (event) {
//                console.log('start', event);
            },
            onEnd: function (event) {
//                console.log('end', event);
//                console.log('from', event.from, event.oldIndex);
//                console.log(event.item);
//                console.log('to', event.to, event.newIndex,);
            }
        },
        computed: {
            cards: {
                get(){
                    return this.pipeLine.cards;
                },
                set(value){
                    console.log('cards', value);
                    this.$store.dispatch('update', {
                        'pipeLineId': this.pipeLine.id,
                        'newCardList': value
                    });
                }
            }
        },
        data() {
            return {
                options: {
                    group: "kanban",
                    animation: 300,
                }
            };
          }
    }

</script>
<style scoped>
    .card-list {
        min-height: 100px;
    }
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