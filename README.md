
# Instalación del servicio para chat y usuario

Primero debes clonar o descargar el [repositorio](https://github.com/j0k3rD/real_time_chat_project)

## Requerimientos

### Instalar Python y Docker:

Este proyecto funciona con python, por lo que hay que descargar e instalar [Python](https://www.python.org/downloads/) en tu sistema operativo.
Y ademas deben instalar [Docker](https://docs.docker.com/get-docker/), para el manejo de microservicios.

## Instalar en Docker los contenedores para Mysql, Redis y Traefik

En Docker, debemos instalar los contenedores para los siguientes servicios, [mysql](https://hub.docker.com/_/mysql) como la versión **mysql:8.0-debian**, luego instalar [redis](https://hub.docker.com/_/redis) con la versión **redis:7.0.9** y por ultimo [traefik](https://hub.docker.com/_/traefik) con la versión **traefik:2.9**.
> docker pull mysql:8.0-debian
> docker pull redis:7.0.9
> docker pull traefik:2.9

Y dejar runeando las tres imagenes con docker compose, que se encuentra dentro del proyecto como **/dockers/traefik**, **/dockers/redis** y **/dockers/mysql**, dentro de estas carpetas escribir el siguiente codigo.

> docker compose up

## Chat Service

### Crear imagen del ChatService:

Para instalar todo los paquetes necesarios, ir a **proyect/chat_service/** y ejecutar en la **terminal** el siguiente comando:

En linux:

> ***install_linux.sh***

En windows:

> ***install_windows.bat***

### Configurar variables locales (dotenv):

Para que el servidor se pueda conectar a la base de datos de nuestro sistema, se debe configurar las variables dentro del .env según nuestro sistema. Para esto, hay que ir a **/dockers/chat_service**, luego duplicar y cambiar de nombre a **.env-example** a **.env** dentro se encuentra lo siguiente:

```
# Key de Django https://docs.djangoproject.com/en/4.1/topics/signing/
SECRET_KEY = 'XXXXXXX'
# Nombre del servicio en traefik.
NAME  =  'chat.chat'

# DATABASE CONFIGURATION 
# Nombre de base de datos en mysql.
DATABASE_NAME  =  ''
# Usuario de base de datos en mysql.
DATABASE_USER  =  ''
# Password de la base de datos en mysql.
DATABASE_PASSWORD  =  ''
# Nombre del servicio de traefik.
DATABASE_HOST  =  'mysql'

# REDIS CONFIGURATION
# Nombre del servicio de traefik del redis.
REDIS_HOST  =  'redis'

# TEMPLATES CONFIGURATION
# Poner la ruta al path de la carpeta static en el proyecto de chat.
STATIC_PATH  =  "**/chat_service/chat/static/"

# CHAT MICROSERVICE CONFIGURATION
# IP del microservicio de chat en traefik.
CHAT_URL  =  'chat.chat.localhost'

# USER MICROSERVICE CONFIGURATION
# IP del microservicio de usuario en traefik.
USER_URL  =  'user.chat.localhost'
```

### Updatear Base de Datos:

Para iniciar el servidor, primero hay que crear la base de datos, en django es muy sencillo, solo hay que ir al directorio **project/chat_service/** y abrir una **terminal** y ejecutar:

En linux:

>***update_database_linux.sh***

En windows:

>***update_database_windows.bat***

### Ejecutar Servidor:

Ya creada la base de datos, solo hay que ejecutar el servidor, escribiendo en la **terminal**:

En linux:

>***boot_linux.sh***

En windows:

>***boot_windows.bat***

## User Service