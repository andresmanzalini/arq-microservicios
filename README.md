# Arquitectura de microservicios 

Funcional, minimalista, escalable y segura

* backend -> Flask Web Server, OAuth2
* bd -> mySQL para usuarios authorizados
* frontend -> React
* nginx -> proxy inverso, load balancer, API Gateway


</br>


## Microservicio Backend

Flask -> Web Server Framework
OAuth2 -> Autenticacion y Autorizacion con Google

Una vez autenticado y autorizado, el usuario puede acceder a las API protegida.

Un usuario autenticado y autorizado puede acceder a info protegida, guardar data, acceder a apis de IA 

Un usuario no logueado solo puede acceder al landing page y hacer algunas pruebas.


</br>


## Microservicio db

mySQL para guardar Auth tokens y Permisos


</br>

## Microservicio nginx 

proxy inverso (load balancer) para comunicacion entre microservicios

extender a API Gateway


</br>

## Microservicio frontend

    . nodejs 
    . React


</br>


## Construir y ejecutar app

```
docker-compose up --build
```

```
docker-compose down
```

</br>


## Estructura del Proyecto

```

├── backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docs
│   ├── errors.md
│   ├── specifications.md
│   └── info.md
├── frontend
│   ├── app.js
│   ├── Dockerfile
│   └── config
├── nginx
│   ├── configs
│   │   ├── default.conf
│   ├── Dockerfile
├── secrets
│   └── client-secret.json
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt

```

</br>

## Diagrama Secuencia Auth

![Diag Seq](diag-seq-auth.png)

</br>

## Observaciones 

. un microservicio backend que se encarga del login, autenticacion y autorizacion con OAuth2.

. una bd con usuarios y autorizaciones 

. un API Gateway nginx que se encarga de manejo de solicitudes

. un microservicio frontend 


el backend se encarga de autenticacion y Authorizacion. 
el problema es que una vez logueado, el cliente necesita usar las credenciales para hacer solicitudes a otros microservicios de la arquitectura.


## Por hacer

. integrar el microservicio frontend

. integrar bd

. guardar usuarios y credenciales en bd

. integrar una queue (rabbitMQ) para comunicar servicios

. integrar MLOps

. optimizar nginx API gateway -> kong API gateway
