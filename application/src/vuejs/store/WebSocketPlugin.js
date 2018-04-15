export default function createWebSocketPlugin (socket) {
    return store => {
        console.log(store, socket);
        socket.onmessage = e => {
            const data = JSON.parse(e.data);
            store.commit('updateList', data)
        };
        store.subscribeAction((action) => {
            console.log(action);
            if (action.type === 'update') {
                socket.send('updateList', action.payload)
            }
        })
    }
}