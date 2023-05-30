# Instalación de Node.js y JavaScript
FROM node:19-alpine AS build

# Soluciona error de incompatibilidad con OpenSSL3.0
ENV NODE_OPTIONS="--openssl-legacy-provider"
ENV SKIP_PREFLIGHT_CHECK=true

# Establecemos el directorio de trabajo
WORKDIR /home/djangoapp/frontend

# Instalamos las dependencias de Node.js
COPY ./frontend/package.json /home/djangoapp/frontend
RUN yarn install

# RUN npm install
COPY ./frontend /home/djangoapp/frontend
RUN yarn build

# Instalamos el servidor web
RUN npm install -g webserver.local

# Obtenemos la imagen de un kernel de Linux con Python y Node.js
FROM python:3.10-slim-bullseye AS production

ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/djangoapp/.local/bin

# Creamos un usuario
RUN useradd --create-home --home-dir /home/djangoapp djangoapp

# Establecemos el directorio de trabajo
WORKDIR /home/djangoapp

# Instalamos las dependencias del sistema
# RUN apt-get update && apt-get install -y curl gcc g++ libffi-dev libssl-dev build-essential default-mysql-client python3-mysqldb libmariadb-dev
RUN apt-get update
RUN apt-get install -y curl gcc g++ libffi-dev libssl-dev build-essential default-mysql-client python3-mysqldb libmariadb-dev
RUN apt-get install -y inetutils-ping
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/*

# Cambiamos al usuario no privilegiado
USER root
RUN mkdir app

# Copiamos los archivos necesarios
COPY ./consul /home/djangoapp/consul
COPY ./user_service /home/djangoapp/user_service
COPY ./user /home/djangoapp/user
COPY ./manage.py /home/djangoapp/
COPY ./entrypoint.sh /home/djangoapp/entrypoint.sh

# Requerimientos de Python
ADD requirements_prod.txt ./requirements.txt
# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos los archivos de la compilación de React
COPY --from=build /home/djangoapp/frontend/build /home/djangoapp/frontend/build

# Exponemos el puerto
EXPOSE 9000

# Ejecutamos el comando de entrada
CMD ["/home/djangoapp/entrypoint.sh"]
