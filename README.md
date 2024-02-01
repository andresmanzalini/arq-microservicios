# App de login y autenticacion con OAuth2.0

arquitectura de 4 microservicios 


<br/>


**backend** 

Flask, OAuth2.0

login y autenticacion con google mediante OAuth2.0


backend workflow -> para trabajar con el backend aislado ir al directorio y trabajar sobre el docker, no sobre el compose

cd backend

seguir las instrucciones del backend/README.md 


**db** 

mySQL


**nginx** 

proxy inverso para comunicacion entr microservicios y cliente


**frontend** 

nodejs 

React?


<br/>


### Construir y ejecutar app

docker-compose up --build


### bajar la app y resetearla

docker-compose down


<br/>

## Estructura del Proyecto

```
├── backend
    ├── app.py
    ├── app_oficial.py
    ├── Dockerfile
    ├── README.md
    └── requirements.txt
├── docs
    ├── errores.md
    ├── especificaciones.md
    └── info.md
├── virtualEnv
├── frontend
    ├── app.js
    ├── Dockerfile
    └── config
├── nginx
    ├── configs
        ├── default.conf
        └── index.js
    ├── asdas.sda
    └── Dockerfile
├── secrets
    └── client-secret.json
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt

```






### Documentacion oficial OAuth 

https://developers.google.com/identity/protocols/oauth2/web-server?hl=es-419#authorization-errors-redirect-uri-mismatch

https://developers.google.com/identity/sign-in/web/server-side-flow?hl=es-419



