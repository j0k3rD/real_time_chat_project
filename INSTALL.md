# Instalación del servicio para chat y usuario

Primero debes clonar o descargar el [repositorio](https://github.com/j0k3rD/real_time_chat_project)

## Requerimientos

### Instalar Python y Docker:

Este proyecto funciona con python, por lo que hay que descargar e instalar [Python](https://www.python.org/downloads/) en tu sistema operativo.

Y ademas deben instalar [Docker](https://docs.docker.com/get-docker/), para el manejo de microservicios.

## Crear red de docker

Vamos a crear una red llamada "red" para conectar todos los contenedores entre sí.

> docker network create red

Para verificar si la red fue creada correctamente, verificar con:

> docker network ls

## Instalar en Docker los contenedores para Mysql, Redis y Traefik

En Docker, debemos instalar los contenedores para los siguientes servicios, [mysql](https://hub.docker.com/_/mysql) como la versión **mysql:8.0-debian**, luego instalar [redis](https://hub.docker.com/_/redis) con la versión **redis:7.0.9** y por ultimo [traefik](https://hub.docker.com/_/traefik) con la versión **traefik:2.9**.

> docker pull mysql:8.0-debian

> docker pull redis:7.0.9

> docker pull traefik:2.9

configurar el .env del mysql, dentro de **/dockers/mysql/.env-example** duplicando el archivo y creando un **.env**, y cambiando lo siguiente:
```
# Nombre de usuario secundario de mysql
MYSQL_USER=
# Contraseña de usuario secundario
MYSQL_PASSWORD=
# Nombre de la base de datos en mysql.
MYSQL_DATABASE=chat_real_time
# Contraseña del usuario root
MYSQL_ROOT_PASSWORD=
```

Y dejar runeando las tres imagenes con docker compose, que se encuentra dentro del proyecto como **/dockers/traefik**, **/dockers/redis** y **/dockers/mysql**, dentro de estas carpetas escribir el siguiente codigo.

> docker compose up

## Chat Service

### Crear imagen del ChatService en Docker:

Antes de crear la imagen, debemos configurar las variables de entorno, hay que ir a **/dockers/chat_service**, luego duplicar y cambiar de nombre de **.env-example** a **.env** dentro se encuentra lo siguiente:

```
# Key de Django https://docs.djangoproject.com/en/4.1/topics/signing/
SECRET_KEY = 'XXXXXXX'

# Nombre del servicio en traefik.
NAME = 'chat.chat'

# DATABASE CONFIGURATION
# Nombre de base de datos en mysql.
DATABASE_NAME = 'chat_real_time'
# Usuario de base de datos en mysql.
DATABASE_USER = ''
# Password de la base de datos en mysql.
DATABASE_PASSWORD = ''
# Nombre del servicio de mysql en traefik.
DATABASE_HOST = 'mysql'
# Puerto del servicio de mysql en traefik
DATABASE_PORT  =  '3306'

# REDIS CONFIGURATION
# Nombre del servicio de redis en traefik.
REDIS_HOST = 'redis'
# Puerto del servicio de redis en traefik.
REDIS_PORT  =  '6378'

# TEMPLATES CONFIGURATION
# Poner la ruta al path de la carpeta static en el proyecto de chat.
STATIC_PATH = "/chat_service/chat/static/"

# CHAT MICROSERVICE CONFIGURATION
# IP del microservicio de chat en traefik.
CHAT_URL = 'http://chat.chat.localhost'

# USER MICROSERVICE CONFIGURATION
# IP del microservicio de usuario en traefik.
USER_URL = 'http://user.chat.localhost'
```

Una ves creado el **.env**, para crear una imagen en Docker debemos entrar en la carpeta **dockers/chat_service** y abrir el archivo **docker-compose.yml** con un editor cualquiera y verificar que versión de chat_service se ejecutara, en nuestro caso, tenemos:
```
version:  '3.3'
services:
	chatservice:
		# container_name: chatservice
		image:  chatservice:v0.3.0
```
En nuestro ejemplo, el nombre de la **image** es *chatservice:v0.3.0* por lo que hay que generar una imagen con ese nombre y versión, para ello hacemos lo siguiente:

Nos vamos a la carpeta **/chat_service** y ejecutamos el siguiente comando:

> docker build -t nombreservicio:version .

en nuestro ejemplo sería:

> docker build -t chatservice:v0.3.0 .

una vez que finaliza, ya tenemos creada nuestra imagen en el Docker, para verificar usamos el comando: 

> docker images

y nos debería aparecer la imagen *chatservice* creada con la versión *0.3.0*. Con eso ya tenemos la imagen creada correctamente.

### Runnear ChatService como contenedor.

Para ejecutar **ChatService**, debemos entrar en la ruta **/dockers/chat_service** y abrir una terminal y ejecutar el siguiente comando

- En caso de querer ejecutar el contenedor en segundo plano:
> docker compose up -d
- En caso de querer ejecutar el contenedor y mostrarlo en la terminal:
> docker compose up

Y con eso ya deberiamos tener el **chatservice** funcionando correctamente en nuestro Docker, para ver si es así, probar con:

> docker ps 

y verificar si la imagen **chat_service** esta corriendo, junto a **traefik, mysql y redis**

## User Service

### Crear Super User en Django: 

Para crear un super usuario y poder editar los grupos, abrir el archivo **entrypoint.sh** y cambiar el contenido descomentando la parte de crear usuario y comentando la parte de runear el servicio

```
#!/bin/bash

# Create superuser
export DJANGO_SUPERUSER_USERNAME=XXXXXXX # Nombre de super usuario, importante, no olvidar
export DJANGO_SUPERUSER_PASSWORD=XXXXXXX # Contraseña del super usuario, importante no olvidar
python3 manage.py createsuperuser --noinput

# Run server
#python3 manage.py migrate
#python3 manage.py runserver 0.0.0.0:9000
```

Y luego generar la imagen *(explicado debajo)* y ejecutarlo, debe decir en la terminal que el **superuser ha sido creado**. Luego dejas comentado la parte de crear el superusuario y descomentas la de ejecutar el servicio. **Recuerda que debes volver a generar la imagen**

### Crear imagen del UserService en Docker:

Antes de crear la imagen, debemos configurar las variables de entorno, hay que ir a **/dockers/user_service**, luego duplicar y cambiar de nombre de **.env-example** a **.env** dentro se encuentra lo siguiente:

```
# Key de Django https://docs.djangoproject.com/en/4.1/topics/signing/
SECRET_KEY = 'XXXXXXX'

# Nombre del servicio en traefik.
NAME = 'user.chat'

# DATABASE CONFIGURATION
# Nombre de base de datos en mysql.
DATABASE_NAME = 'chat_real_time'
# Usuario de base de datos en mysql.
DATABASE_USER = ''
# Password de la base de datos en mysql.
DATABASE_PASSWORD = ''
# Nombre del servicio de mysql en traefik.
DATABASE_HOST = 'mysql'
# Puerto del servicio de mysql en traefik
DATABASE_PORT  =  '3306'

# REDIS CONFIGURATION
# Nombre del servicio de redis en traefik.
REDIS_HOST = 'redis'
# Puerto del servicio de redis en traefik.
REDIS_PORT  =  '6378'

# TEMPLATES CONFIGURATION
# Poner la ruta al path de la carpeta static en el proyecto de chat.
STATIC_PATH = "/user_service/chat/static/"

# CHAT MICROSERVICE CONFIGURATION
# IP del microservicio de chat en traefik.
CHAT_URL = 'http://chat.chat.localhost'

# USER MICROSERVICE CONFIGURATION
# IP del microservicio de usuario en traefik.
USER_URL = 'http://user.chat.localhost'

# REDIS CONFIGURATION
# IP del redis en Docker.
REDIS_CACHE_URL = 'redis://redis:6379/1'
```

Una ves creado el **.env**, para crear una imagen en Docker debemos entrar en la carpeta **dockers/user_service** y abrir el archivo **docker-compose.yml** con un editor cualquiera y verificar que versión de chat_service se ejecutara, en nuestro caso, tenemos:
```
version:  '3.3'
services:
	chatservice:
		# container_name: chatservice
		image:  userservice:v0.3.0
```
En nuestro ejemplo, el nombre de la **image** es *userservice:v0.3.0* por lo que hay que generar una imagen con ese nombre y versión, para ello hacemos lo siguiente:

Nos vamos a la carpeta **/user_service** y ejecutamos el siguiente comando:

> docker build -t nombreservicio:version .

en nuestro ejemplo sería:

> docker build -t userservice:v0.3.0 .

una vez que finaliza, ya tenemos creada nuestra imagen en el Docker, para verificar usamos el comando: 

> docker images

y nos debería aparecer la imagen *userservice* creada con la versión *0.3.0*. Con eso ya tenemos la imagen creada correctamente.

### Runnear UserService como contenedor.

Para ejecutar **UserService**, debemos entrar en la ruta **/dockers/user_service** y abrir una terminal y ejecutar el siguiente comando

- En caso de querer ejecutar el contenedor en segundo plano:
> docker compose up -d
- En caso de querer ejecutar el contenedor y mostrarlo en la terminal:
> docker compose up

Y con eso ya deberiamos tener el **userservice** funcionando correctamente en nuestro Docker, para ver si es así, probar con:

> docker ps 

y verificar si la imagen **user_service** esta corriendo, junto a **traefik, mysql y redis**

## Probar servicios y configurar grupos

Para probar si todo esta funcionando correctamente, debes ingresar a [chat.chat.localhost/admin](https://chat.chat.localhost/admin) e ingresar el usuario y contraseña de admin de django creado anteriormente.
Y luego creado un nuevo grupo siguiendo el ejemplo de la siguientes imágenes:
- Primero debemos entrar a la tabla de **Groups** en nuestra base de datos
![Ingresar a grupo](https://i.ibb.co/XVTzwFG/image.png)
- Luego *agregar un nuevo grupo* apretando **Add Group +**
![agregar grupo](https://i.ibb.co/ZWMmCTd/image2.png)
- Luego *ingresar un nombre de grupo* en este ejemplo es **Grupo Prueba** y *guardarlo* apretando **Save**
![crear grupo prueba](https://i.ibb.co/jgbnsnj/image3.png)
- Y por ultimo verificamos que el grupo esta creado correctamente con **Group object (1)**
![grupo prueba creado](https://i.ibb.co/b6yv3d1/image4.png)

Ya con el grupo creado podemos ingresar a la página [user.chat.localhost/login](https://user.chat.localhost/login), registrarse con una cuenta, luego loguearse, entrar al chat que creamos anteriormente y escribir en el chat. 
> Tener en cuenta que el **Admin**, es el único que puede crear y eliminar grupos desde [chat.chat.localhost/admin](https://chat.chat.localhost/admin) utilizando el ejemplo anterior de crear un grupo.

## Posibles errores y soluciones:

### home/djangoapp/entrypoint.sh no such file or directory:
En caso de encontrarte el error de **/entrypoint.sh** no encontrado el archivo o directorio, es un problema de permisos, la solución depende segun sistema operativo:
- Windows: En caso del sistema operativo Windows, es eliminar y volver a crear el archivo **/entrypoint.sh** dentro del **user_service** o **chat_service** segun que contenedor este dando el error. 
- Linux: En caso del sistema operativo Linux, la solución es darle permisos por **chmod** al **/entrypoint.sh** dentro del **user_service** o **chat_service** segun que contenedor este dando el error.
> chmod 777 entrypoint.sh

**En caso de que lo anterior no funcione**, agradecimientos totales a **Diego Alejandro Conde** en compartir solución, en resumen es ingresar el siguiente comando en **terminal** 
> git config --global core.autocrift input

![error entrypoint](https://i.ibb.co/4tZxgdh/error.png)

**Recuerda que al hacer estos cambios, hay que volver a generar la imagen y ejecutarlo en Docker para arreglar el problema**