cd user_service/
# Creamos la imagen de Docker. Debemos editar la version cada vez que implementemos algo nuevo en el servicio
docker build -t userservice:v0.4.0 .