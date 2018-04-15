export default function createWebSocketPlugin (socket) {
    return store => {
        console.log(store, socket);
        // サーバからの返答をもってmutationする
        socket.onmessage = e => {
            const data = JSON.parse(e.data);
            store.commit(data.type, data)

        };
        // ActionをPlugin側でHookしてwsに投げる
        store.subscribeAction((action) => {
            console.log(action);
            if (action.type === 'update') {
                socket.send(JSON.stringify({
                    type: 'update',
                    payload: action.payload
                }))
            }
        })
    }
}