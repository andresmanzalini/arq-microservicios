# Arquitectura de Microservicios

backend se encarga de login y autenticacion con Flask y OAuth2.0

frontend es el cliente, y se comunica con el backend

db se comunica con backend

nginx comunica frontend con backend


(imagen arq. microservicios)


### estructura del proyecto

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


ESpecificar cada microservicio

