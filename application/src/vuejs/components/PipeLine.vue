<template>
    <div class="pipeline">
        <div class="pipeline-title">
            {{pipeLine.title}} count: {{pipeLine.cards.length}}
            <button class="close-button" @click="addCard">+</button>
        </div>
        <div class="card-list">
            <draggable :options="options" v-model="cards" class="card-draggable-base">
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
            addCard(){
                let title = window.prompt('title');
                if(title === undefined || title === null){
                    return;
                }
                this.$store.dispatch('add_card', {
                    'pipeLineId': this.pipeLine.id,
                    'title': title,
                    'order': this.pipeLine.cards.length,
                });
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
    .card-draggable-base {
        min-height: 100px;
    }
    .pipeline {
        margin: 5px;
        padding: 5px;
        width: 200px;
        border: solid;
    }
    .pipeline-title {
        text-align: center;
        padding: 5px;
        border: solid;
    }
    .close-button {
        width: 30px;
        height: 30px;
        border: solid;
        cursor: pointer;
    }

</style>