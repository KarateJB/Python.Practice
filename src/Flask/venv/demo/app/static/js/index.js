Vue.use(new VueSocketIO({
    debug: true,
    connection: Vue.prototype.$serverAddr //'http://localhost:5000'
}))


var app = new Vue({
    el: "#app",
    sockets: {
        connect: function () {
            this.appendLog("Start connect...");
            this.$socket.emit('connected_event', { data: 'WebSocket connected successfully.' });
        },
        server_response: function (msg) {
            this.appendLog(msg.data);
        }
    },
    data: {
        clientMsg: "",
        log: "",
    },
    methods: {
        emitMsg: function () {
            this.$socket.emit('broadcast_event', { data: this.clientMsg });
        },
        appendLog: function (newLog) {
            this.log += newLog + "\n";
        }
    },
    created: function () {
    }
})