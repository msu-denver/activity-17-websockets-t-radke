const HOST = '127.0.0.1';
const PORT = 4000;
const socket = new WebSocket('ws://' + HOST + ':' + PORT);

socket.onopen = function(event) {
    console.log('Connected to WebSocket server.');
};

socket.onmessage = function(event) {
    const messagesDiv = document.getElementById('messages');
    const message = document.createElement('div');
    message.textContent = event.data;
    messagesDiv.appendChild(message);
};

socket.onclose = function(event) {
    console.log('Disconnected from WebSocket server.');
};

socket.onerror = function(error) {
    console.error('WebSocket error:', error);
};

function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value;
    socket.send(message);
    input.value = '';
}
