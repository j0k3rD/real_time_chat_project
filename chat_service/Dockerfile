# Instalación de Node.js
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
RUN npm install -g webserver.local

#obtenemos la imagen de un kernel de Linux con python
FROM python:3.10-slim-bullseye AS production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/djangoapp/.local/bin

#crea usuario
RUN useradd --create-home --home-dir /home/djangoapp djangoapp

#seleccionar la carpeta de usuario
WORKDIR /home/djangoapp
#instala dependencias del sistema
RUN apt-get update

#! AGREGAR AQUI LAS DEPENDENCIAS REDIS??
RUN apt-get install -y curl gcc g++ libffi-dev libssl-dev build-essential default-mysql-client python3-mysqldb libmariadb-dev
RUN apt-get install -y inetutils-ping

RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/*

USER djangoapp
RUN mkdir app
#copia la carpeta del proyecto a la imagen
COPY ./chat_service /home/djangoapp/chat_service
COPY ./chat /home/djangoapp/chat
COPY ./manage.py /home/djangoapp/
COPY ./entrypoint.sh /home/djangoapp/entrypoint.sh

# Requerimientos de Python
ADD requirements_prod.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install gevent gunicorn==20.1.0

# Copiamos los archivos de la compilación de React
COPY --from=build /home/djangoapp/frontend/build /home/djangoapp/frontend/build

#puerto por el que escucha la imagen
EXPOSE 7000

CMD ["/home/djangoapp/entrypoint.sh"]