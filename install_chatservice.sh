cd chat_service/
# Creamos la imagen de Docker. Debemos editar la version cada vez que implementemos algo nuevo en el servicio
docker build -t chatservice:v0.6.0 .