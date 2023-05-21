# Obtenemos la imagen de un kernel de Linux con Python y Node.js
FROM python:3.10-slim-bullseye

# Instalamos las dependencias del sistema
RUN apt-get update && apt-get install -y curl gcc g++ libffi-dev libssl-dev build-essential default-mysql-client python3-mysqldb libmariadb-dev

# Creamos un usuario
RUN useradd --create-home --home-dir /home/djangoapp djangoapp

# Establecemos el directorio de trabajo
WORKDIR /home/djangoapp

# Copiamos los archivos necesarios
COPY ./user_service /home/djangoapp/user_service
COPY ./user /home/djangoapp/user
COPY ./manage.py /home/djangoapp/
COPY ./entrypoint.sh /home/djangoapp/entrypoint.sh

# Copiamos la carpeta 'frontend'
COPY ./frontend /home/djangoapp/frontend

# Instalamos las dependencias de React
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Limpiamos la caché de NPM
RUN npm cache clean --force

# Instalamos las dependencias de React
RUN npm install

# Cambiamos al directorio de la aplicación React
WORKDIR /home/djangoapp/frontend

# Ejecutamos el comando npm run build para generar los archivos estáticos
RUN npm run build

# Copiamos los archivos estáticos generados al directorio apropiado en la imagen final
RUN cp -r build/* /home/djangoapp/user/static/

# Volvemos al directorio principal del proyecto
WORKDIR /home/djangoapp

# TODO: Cambiar por requirements_production.txt
ADD requirements_prod.txt ./requirements.txt

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Cambiamos al usuario no privilegiado
USER djangoapp

# Exponemos el puerto
EXPOSE 9000

# Ejecutamos el comando de entrada
CMD ["/home/djangoapp/entrypoint.sh"]
