
const DEFAULT_DATA = [
            {
                name: 'TODO',
                id: 1,
                cards: [
                    {
                        id: 1,
                        content: 'a',
                    },
                    {
                        id: 2,
                        content: 'b',
                    },
                    {
                        id: 3,
                        content: 'c',
                    },
                ]
            },
            {
                name: 'DOING',
                id: 2,
                cards: [
                    {
                        id: 4,
                        content: 'd',
                    },
                    {
                        id: 5,
                        content: 'e',
                    },
                ]
            },
            {
                name: 'DONE',
                id: 3,
                cards: [
                    {
                        id: 6,
                        content: 'f',
                    },
                    {
                        id: 7,
                        content: 'g',
                    },
                ]
            },

        ];


const store = {
    state: {
        pipeLineList: DEFAULT_DATA,
    },
    actions: {
        reset(context){
            console.log('reset');
            context.commit('resetList');
        },
        update(context, payload){
            context.commit('updateList', payload)
        }
    },
    mutations: {
        updateList (state, payload) {
            console.log('updateList', state, payload);
            let pipeLineId = payload.pipeLineId;
            let newCardList = payload.newCardList;
            for(let pipeLine of state.pipeLineList){
                if(pipeLine.id === pipeLineId){
                    pipeLine.cards = newCardList;
                }
            }


        }
    }
};

export default store;