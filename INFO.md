# Diseño del Sistema
El sistema funciona mediante requests, teniendo un Backend encargado del manejo de la base de datos y partes logicas y de un Frontend el cual se comunica con el cliente mediante una pagina web.
## User
El usuario se encarga de conectarse a nuestro microservicio de logueo y al loguearse correctamente es redirigido al microservicio del chat.
## Chat
El es encargado de mostrar al usuario los diferentes tipos de grupos a unirse una ves logueado, y al elegir un grupo recibir los datos escritos en ese grupo almacenado en una base de datos, y darle al usuario la posibilidad de escribir lo que quiera dentro y mostrado a los demás usuarios conectados. Una ves que cierra la página o se desloguea es redireccionado al microservicio de logueo.
El chat tiene un sistema de token, para evitar que un usuario no registrado acceda al chat de los grupos.