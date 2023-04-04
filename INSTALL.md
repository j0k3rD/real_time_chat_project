# Instalación del servicio para chat y usuario

Primero debes clonar o descargar el [repositorio](https://github.com/j0k3rD/real_time_chat_project)

## Chat

### Instalar python y base de datos:

Este proyecto funciona con python, por lo que hay que descargar e instalar [python](https://www.python.org/downloads/) en tu sistema operativo.

Y ademas debes instalar alguna base de datos para el almacenamiento de datos, puedes instalar **mysql comunity server** y **mysql workbench** [aquí](https://dev.mysql.com/downloads/)

### Crear entorno virtual:

Antes hay que crear un entorno virtual, para instalar todo lo necesario del requirements.txt. Para crear un entorno virtual utilizando python y venv [entra aquí.](https://docs.python.org/es/3.8/library/venv.html)

### Instalar requerimientos:

Para instalar todo los paquetes necesarios, ir a **proyect/chat_service/** y ejecutar en la **terminal** el siguiente comando:
En linux:
> ***install_linux.sh***

En windows:
> ***install_windows.bat***

### Configurar variables locales (dotenv):

Para que el servidor se pueda conectar a la base de datos de nuestro sistema, se debe configurar las variables dentro del .env según nuestro sistema. Para esto, hay que ir a **project/chat_service/chat_service/**, luego duplicar y cambiar de nombre a **.env-example** a **.env** dentro se encuentra lo siguiente:

```

# Key de Django https://docs.djangoproject.com/en/4.1/topics/signing/

SECRET_KEY = 'XXXXXXX'

# Nombre de la base de datos

DATABASE_NAME = 'chat_real_time'

# Usuario de la base de datos

DATABASE_USER = 'root'

# Password de la base de datos

DATABASE_PASSWORD = 'XXXXXXX'

# IP de la base de datos

DATABASE_HOST = 'localhost'

# Puerto de la base de datos

DATABASE_PORT = ''

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