# App de login y autenticacion con OAuth2.0

arquitectura de 3 microservicios

**backend** 

Flask, OAuth2.0

login y autenticacion con google mediante OAuth2.0


**frontend** 

nodejs, React?


**db** 

mySQL


**nginx** 

proxy inverso para comunicacion entr microservicios y cliente



<br/>


## Construir y ejecutar app

docker-compose up --build


## bajar la app y resetearla

docker-compose down

docker volume rm micro-auth-bd-docker_db_data



<br/>

## Microservicios


### backend

flujo para laburar con app

para trabajar con el backend aislado ir al directorio y trabajar sobre el docker, no sobre el compose

cd backend

docker build

docker run 





### FALTA

#### monitor

cuando se tira un docker-compose up  se abra 1 terminal por cada microservicio

en vez de mostrar todo en la misma consola, estaria bueno que se muestre en 1 cinsola por miroservicio


### BUGS

BUG 1: el 1er inicio es automatico.

recuerda la sesion

verificar bien el 1er ingreso
el problema es en el manejo del Ctrl + C para apagar el servidor

es un handler_shutdown()
y hay que manejarlo mediante una señal SIGNAL

esa señal debe ser Ctrl + C 

al apretar Ctrl C , antes de apagar el servidor se debe ejecutar handler_shutdown()






### Documentacion oficial OAuth 

https://developers.google.com/identity/protocols/oauth2/web-server?hl=es-419#authorization-errors-redirect-uri-mismatch

https://developers.google.com/identity/sign-in/web/server-side-flow?hl=es-419




continuar con la utilización de las credenciales para acceder a los recursos protegidos por la API de Google en nombre del usuario.

