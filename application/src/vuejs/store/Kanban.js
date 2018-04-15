import createWebSocketPlugin from './WebSocketPlugin';

const socket = new WebSocket('ws://' + window.location.host + '/ws' + window.location.pathname);
const plugin = createWebSocketPlugin(socket);


const store = {
    state: {
        pipeLineList: [],
        kanbanId: parseInt(window.location.pathname.split('kanban/')[1])
    },
    actions: {
        add_pipeline(context, payload){
            console.log('action add_pipeline called', payload);
        },
        add_card(context, payload){
            console.log('action add_card called', payload);
        },
        update(context, payload){
            // 実際のcommitはplugin側にたくしている
            // 定義しないとdispatchできないので・・・
            console.log('action update called', payload);
            //context.commit('update', payload)
        }
    },
    mutations: {
        set_data(state, payload){
            console.log('set_data', state, payload);
            this.state.pipeLineList = payload.kanban;
        },
        update(state, payload) {
            console.log('update', state, payload);
            let pipeLineId = payload.pipeLineId;
            let newCardList = payload.newCardList;
            for(let pipeLine of state.pipeLineList){
                if(pipeLine.id === pipeLineId){
                    pipeLine.cards = newCardList;
                }
            }
        }
    },
    plugins: [plugin]
};

export default store;