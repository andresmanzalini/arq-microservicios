# App de login y autenticacion con google usando OAuth2.0

arquitectura de 3 microservicios

backend -> Flask, OAuth2.0

frontend -> nodejs, React?

db -> mySql

nginx -> proxy inverso para comunicacion entr microservicios y cliente


## app

basicamente consiste en login con google mediante oAuth2.0

## bd

almacena la data que se le sacude desde el browser

datetime corrido , pero va


<br/>


## Construir  y ejecutar app

docker-compose up --build


. bajar la app y resetearla

docker-compose down

docker volume rm micro-auth-bd-docker_db_data


. ejecutar app

docker-compose up -d


<br/>

## Microservicios

### bd

con el servidor ejecutando, abrir una terminal


1. ingresar al contenedor

    docker-compose exec db bash


2. conectarse a la instancia mysql

    mysql -u root -p


3. inspeccionar la bd

    SHOW DATABASES;
    USE nueva_BD;
    SHOW TABLES;
    SELECT * FROM sesiones;


<br/>


#### microservicio backend

flujo para laburar con app

abrir terminal

1. abrir contenedor de app

    docker-compose exec backend bash

2. inicializar la bd. 
este paso es solo en el 1er uso
    
    flask db init

crea database nueva_BD


3. migrar datos de la bd

    flask db migrate

    flask db upgrade


4. observar

    docker-compose logs -f backend




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



## completada la etapa de obtención y almacenamiento de las credenciales

## listo para continuar con la utilización de las credenciales para acceder a los recursos protegidos por la API de Google en nombre del usuario.

