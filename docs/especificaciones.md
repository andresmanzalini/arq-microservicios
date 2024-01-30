# Arquitectura de Microservicios

backend se encarga de login y autenticacion con Flask y OAuth2.0

frontend es el cliente, y se comunica con el backend

db se comunica con backend

nginx comunica frontend con backend


(imagen arq. microservicios)


## estructura del proyecto

arq-microservicios
    |-backend/
        |-app.py
        |-Dockerfile
        |-requirements.txt
    |-db
        |-db_data
    |-docs
        |-arquitectura.png
        |-especificaciones.md
    |-env/
        |-backend.env
        |-asdas.env
    |-frontend/
        |-app/
            |-node_modules
            |-public
            |-src/
            |-README.md
        |-nginx/
            |-default.conf
        |-Dockerfile
    |-nginx/
        |-configs/
            |-default.conf
        |-Dockerfile
    |-venv
    |-docker-compose.yml
    |-README.md
    |-requirements.txt



## crear en google.console proyecto y cliente OAuth

1. https://console.cloud.google.com/

2. Nuevo Proyecto -> nombre -> crear proyecto -> seleccionar prouyecto

3. Configurar pantalla de CONSENTIMIENTO

3.1 Pantalla de consentimiento
    3.1.1 externo -> crear
    3.1.2 nombre app , email , info contacto desarrollador
    3.1.3 guardar y continuar

3.2 Permisos
    3.2.1 agregar o quitar permisos -> seleccionar permisos -> actuaizar
    3.2.2 guardar y continuar

3.3 Usuarios de Prueba **!ACA!**
    3.3.1 add user -> usuario@gmail.com -> agregar usuario
    3.3.2 guardar y continuar

agregar los usuarios de prueba de la app. esos usuarios saltan el error acces_denied

volver al panel


4. Credenciales

4.1 Crear credenciales -> id cliente OAuth

4.2 crear id cliente OAuth
4.2.1 tipo aplicacion -> aplicacion web ,  nombre
4.2.2 URI de redireccionamiento autorizado -> agregar URI -> http://127.0.0.1:5000/api/callback
4.2.3 crear
4.2.4 descargar json -> aceptar
descarga client-secret.json 
pegar ese archivo en arq-microservicios/secrets

listo, ya se puede usar ese cliente OAuth de prueba , el cual es redirigido al callback endpoint especificado en 4.2.2



## Microservicios

## backend

se puede trabajar de forma aislada o en conjunto

de forma asiada, entrar en el directorio backend y trabajar en el Dockerfike
hay documentacion especifica en README.md


en conjunto, ejecutar el docker compose


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




## frontend

Los comandos npm install, COPY app ./ y npm run build son utilizados para construir tu aplicación React dentro del contenedor Docker. Aquí está cómo funcionan cada uno de estos comandos:

npm install: Este comando instala las dependencias de tu aplicación. Utiliza el archivo package.json y package-lock.json (si existe) para determinar las dependencias y sus versiones. Esto asegura que las dependencias requeridas estén disponibles en el entorno del contenedor.

COPY app ./: Este comando copia el contenido del directorio local app (que probablemente contiene tu código fuente y archivos de configuración) al directorio de trabajo /app dentro del contenedor. Esto incluirá también los archivos package.json y package-lock.json que copiaste anteriormente.

npm run build: Este comando ejecuta el script de construcción definido en tu archivo package.json. En la mayoría de las aplicaciones React generadas por Create React App (CRA), este script ejecutará la compilación de la aplicación para producción, creando una versión optimizada y lista para ser desplegada.

En resumen, estos comandos realizan el proceso de construcción de tu aplicación React dentro del contenedor Docker, lo que te permite empaquetar la aplicación y sus dependencias en una imagen que puedes desplegar fácilmente en cualquier entorno compatible con Docker.



## bd

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

