<template>
    <div class="card">
        {{ card.content }}
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
        padding: 5px;
        border: solid;
        cursor: move;
    }

</style>