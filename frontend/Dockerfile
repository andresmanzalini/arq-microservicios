# Etapa de construcción
FROM node:14 as build

WORKDIR /app

COPY app/package*.json ./

RUN npm install

COPY app ./

RUN npm run build


# Etapa de producción
FROM nginx

EXPOSE 3000
#cualquier trafico desde nginx server va a ser forwardeado a este microservicio frontend, escuchado en el 3000
COPY /nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html


## Comando para iniciar el servidor web de Nginx
##CMD ["nginx", "-g", "daemon off;"]
