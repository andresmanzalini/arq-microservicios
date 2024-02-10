# Arq microservicios 

## Autenticacion y autorizacion con OAuth2.0

1. Autenticacion
2. Autorizacion

implementa el protocolo OAuth2

Una vez autenticado y autorizado, el usuario puede acceder a la seccion protegida




<br/>


## backend

tecnologias:
    . Flask, para web server minimalista 
    . OAuth2.0 , para autenticacion y autorizacion con google usando OAuth2


. autenticacion con google account mediante OAuth2

. autorizacion para acceder a las API de Google


un usuario autenticado y autorizado puede acceder a info protegida, guardar data protegida, tratamiento personalizado con IA de recomendacion.

un usuario no logueado solo puede acceder a muestras, pero no tiene IA personalizada de recomendacion ni guarado persistente de data



## db

tecnologias:
    . mySQL para guardar Authorizaciones y Permisos


## nginx 

proxy inverso (load balancer) para comunicacion entr microservicios


## frontend

tecnologias:
    . nodejs 
    . React


<br/>


### Construir y ejecutar app

docker-compose up --build

docker-compose down


<br/>


## Estructura del Proyecto

```

├── authentication-service
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── documentation
│   ├── errors.md
│   ├── specifications.md
│   └── info.md
├── frontend-service
│   ├── app.js
│   ├── Dockerfile
│   └── config
├── nginx-proxy
│   ├── configs
│   │   ├── default.conf
│   │   └── index.js
│   ├── Dockerfile
├── secrets
│   └── client-secret.json
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt

```

</br>

### Por hacer

optimizar el diseno y la impementacion

convertir en una API Gateway
