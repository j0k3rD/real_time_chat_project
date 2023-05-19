// Obtener el nombre del grupo por medio del id
const groupID = JSON.parse(document.getElementById('group-id').textContent);
const username = JSON.parse(document.getElementById('username').textContent);
const userID = JSON.parse(document.getElementById('user-id').textContent);

// Conectar al grupo
var wss = new WebSocket(
    'wss://' 
    + window.location.host
    + '/wss/chat/group/'
    + groupID
    + '/'
);

// Conectar al grupo
wss.onopen = function(e) {   
    console.log('Connection established');
};

// Función para hacer scroll hacia abajo en el chat
function scrollToBottom() {
    const chatLog = document.getElementById('message_box');
    chatLog.scrollTop = chatLog.scrollHeight;
};

// Recibir datos del chat
wss.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const chatLog = document.getElementById('chat-log');

    // Verifica si el remitente del mensaje es el usuario actual
    if (data.username === username) {
        // Agregar mensaje al template del chat
        chatLog.innerHTML += `
            <li class="clearfix">
                <div class="message-data text-right">
                    <span class="message-data-time">10:10 AM, Today</span>
                    <img src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="avatar">
                    <span>You:</span>
                </div>
                <div class="message other-message float-right">${data.message}</div>
            </li>
        `;
    } else {
        chatLog.innerHTML += `
            <li class="clearfix">
                <div class="message-data">
                    <span class="message-data-time">10:10 AM, Today</span>
                    <img src="https://bootdey.com/img/Content/avatar/avatar2.png" alt="avatar">
                    <span>${data.username}:</span>
                </div>
                <div class="message my-message">${data.message}</div>
            </li>
        `;
    }

    // Hacer scroll hacia abajo para mostrar el último mensaje
    scrollToBottom();
};

// Desconectar del grupo
wss.onclose = function(e) {
    console.log('Connection closed');
};

// Enviar datos del chat
document.getElementById('chat-form').onsubmit = function(e) {
    e.preventDefault();
    const message = document.getElementById('form_message').value;
    
    if (message === '') {
        alert('Please enter a message.');
        return;
    }
    
    wss.send(JSON.stringify({
        'message': message,
        'username': username,
        'user_id': userID,
    }));

    // Limpiar el campo de entrada después de enviar el mensaje
    document.getElementById('form_message').value = '';
};