# App de login y autenticacion con OAuth2.0

arquitectura de 4 microservicios 


**backend** 

Flask, OAuth2.0

login y autenticacion con google mediante OAuth2.0


**db** 

mySQL


**nginx** 

proxy inverso para comunicacion entr microservicios y cliente


**frontend** 

nodejs 

React?




<br/>


## Construir y ejecutar app

docker-compose up --build


## bajar la app y resetearla

docker-compose down

docker volume rm micro-auth-bd-docker_db_data



<br/>

## Microservicios


### backend

app workflow

para trabajar con el backend aislado ir al directorio y trabajar sobre el docker, no sobre el compose

cd backend

y seguir las instrucciones del backend/README.md 


<br/>



## FALTA

### monitor

cuando se tira un docker-compose up  se abra 1 terminal por cada microservicio

en vez de mostrar todo en la misma consola, estaria bueno que se muestre en 1 cinsola por miroservicio


### acceso protegido a recursos de usuario 

bearer

jwt




### Documentacion oficial OAuth 

https://developers.google.com/identity/protocols/oauth2/web-server?hl=es-419#authorization-errors-redirect-uri-mismatch

https://developers.google.com/identity/sign-in/web/server-side-flow?hl=es-419



