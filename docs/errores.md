# Errores recurrentes y espeficiso


## Error 1 : Permisos

contexto:
luego de crear un secreto en el compose, ejecuto el docker-compose up y empieza a construir.
y en una de esas me pide permiso para acceder a mis documentos.
le digo NO.
y de ahi surge el error

Container backend  Recreate                                                                                                                    0.2s 
Error response from daemon: invalid mount config for type "bind": stat /host_mnt/Users/andresmanzalini/Documents/Proyectos/Arquitectura/arq-microservicios/client-secret.json: operation not permitted


soluciones: 

. recinicar el docker y prune -> NO

. agregar la direccion a docker desktop / shared files -> NO

. docker-credentials-desktop erase -> NO

. reiniciar las credenciales ? no

. darle permiso al SO! desde configuracion ! SI IDOLO!


solucion:
Originalmente denegaste el permiso de acceso a la carpeta "Documentos" durante el proceso de construcción del contenedor, 
Docker Desktop podría no tener permisos para acceder a ese directorio.

Concede Acceso a Documentos:

Si previamente denegaste el acceso a "Documentos", revierte esa decisión.

Abrir Preferencias del Sistema desde el menú de Apple en la esquina superior izquierda de la pantalla.

Selecciona "Seguridad y privacidad".

Ve a la pestaña "Privacidad".

En el lado izquierdo, encontrarás una lista de categorías. Selecciona "Archivos y carpetas".

En el lado derecho, deberías ver una lista de aplicaciones que han solicitado acceso a diversas carpetas.

Haz clic en el icono de candado en la esquina inferior izquierda para desbloquear la configuración.

Ingresa tu contraseña cuando se te pida.

A continuación, debes poder hacer clic en el botón "+" para agregar aplicaciones.

Selecciona "Docker" en la lista de aplicaciones.

Ahora deberías ver Docker agregado a la lista con acceso a la carpeta Documentos.


BIEN!


------------------------------------------------------------------------------------------------

## Error 2 : Secretos

solucionado

explicar docker secrets

y como accedeelo desde la app

------------------------------------------------------------------------------------------------

## Error 3 : acces denied

api login funciona

genera el url de redireccionamiento

y aho, entre apilogin y api/callback falla por un problema de permisos denegado

. cambie el proyecto de google cloud -> nada


backend  | INFO:werkzeug:192.168.65.1 - - [28/Jan/2024 18:44:47] "GET /api/login HTTP/1.1" 302 -