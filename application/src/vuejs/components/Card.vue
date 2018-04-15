<template>
    <div class="card">
        <div class="card-title">{{card.title}}</div>
        <div>
            {{card.content}}
        </div>
    </div>
</template>
<script>

    export default {
        name: 'Card',
        props: [
            'card',
        ]
    }

</script>
<style scoped>
    .card {
        margin: 5px;
        border: solid;
        cursor: move;
    }
    .card-title {
        background-color: #333333;
        color: #fffccf;
    }

</style>