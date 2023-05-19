// Scrollea al final del chat cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    var messageBox = document.getElementById('message_box');
    messageBox.scrollTop = messageBox.scrollHeight;
  });
