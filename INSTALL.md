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

### Crear Super User en Django: 

Para crear un super usuario y poder editar los grupos, abrir el archivo **entrypoint_superuser.sh** y cambiar el contenido en

```
#!/bin/bash

# Create superuser
export DJANGO_SUPERUSER_PASSWORD=XXXXXXX # Contraseña del super usuario, importante no olvidar
export DJANGO_SUPERUSER_USERNAME=XXXXXXX # Nombre de super usuario, importante, no olvidar
export DJANGO_SUPERUSER_EMAIL=XXXXXXX 	 # Email del superusuario, esto no es muy necesario
python3 manage.py createsuperuser --noinput
```

Y luego cambiar el nombre de **entrypoint.sh** a **entrypoint1.sh** y de **entrypoint_superuser.sh** a **entrypoint.sh**, seguir todos los pasos de abajo crear imagen y runear la imagen, luego parar el container, eliminar la imagen y cambiar de nombre **entrypoint1.sh** a **entrypoint.sh**, generar imagen y correrlo. (Si hay una mejor manera de hacer esto, cambiarlo)

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

### Configurar variables locales (dotenv) y configurar la base de datos (Esto es en caso de querer hacer testeos desde una computadora local):

Primero debemos configurar la base de datos y crear los modelos necesarios para funcionar con el **user_service**, por lo que nos vamos a la carpeta **/user_service/user_service**, luego duplicamos y cambiamos el nombre de **env-example** a **env** y cambiar los valores dentro por los siguientes:

```
# Key de Django https://docs.djangoproject.com/en/4.1/topics/signing/
SECRET_KEY  =  ''

# DATABASE CONFIGURATION
# Nombre de la base de datos en mysql.
DATABASE_NAME  =  'chat_real_time'
# Nombre de usuario secundario de mysql.
DATABASE_USER  =  ''
# Contraseña de usuario secundario de mysql.
DATABASE_PASSWORD  =  ''
# IP de mysql corriendo en docker, se puede obtener con el siguiente comando
(docker network inspect bridge --format='{{json .Containers}}' | jq -r '.[] | .Name + " " + .IPv4Address').
DATABASE_HOST  =  'xxx.xxx.xxx.xxx'
DATABASE_PORT  =  '3306'

# REDIS CONFIGURATION
# IP de redis corriendo en docker.
REDIS_HOST  =  'xxx.xxx.xxx.xxx'
REDIS_PORT  =  '6378'

# TEMPLATES CONFIGURATION
# Utilizado para redireccionar los estilos estaticos y templates.
STATIC_PATH  =  "/user_service/chat/static/"

# CHAT MICROSERVICE CONFIGURATION
CHAT_URL  =  'http://chat.chat.localhost'

# USER MICROSERVICE CONFIGURATION
USER_URL  =  'http://user.chat.localhost'

# ADMIN TOKEN CONFIGURATION
# Nombre del admin de Django que creamos anteriormente en el ChatService
USERNAME_DATA = ''
# Contraseña del admin de Django que creamos anteriormente en el ChatService
PASSW_DATA = ''
```

Ya con eso, tenemos nuestra base de datos **chat_real_time** dentro de mysql creado y configurado correctamente para funcionar con **UserService**! 

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