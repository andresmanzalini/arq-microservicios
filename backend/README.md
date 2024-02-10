# Microservicio Backend

Flask App
    . app,py es la app simple de autenticacion y autorizacion de nombre, email
    . app_oficial.py ers la app de demostracion de l;a documentacion oficial de google

OAuth2.0
    . autentica y autoriza con google


(diagrama de secuencias de login )


</br>

## Construir backend aislado

docker build -t backend .


## Ejecutar Backend aislado

docker run -p 5000:5000 backend


</br>


## Endpoints

**/**

home / contiene todos los endpoints alcanzados por el inicio.

en este caso home solo alcanza al endpoint /api/login

lo alcanza mediante la accion/evento de apretar el boton de login



**/api/login**

este endpoint se activa al apretar el boton login 

redirige al usuario a google accounts

el usuario se loguea (autenticacion) y luego autoriza a la app (autorizacion)

una vez que el usuario da el ok, toma la posta el servidor de google OAuth2

verifica que el usuario tenga permisos.
de ser asi, redirecciona al usuario al endpoint /api/callback definido en google cloud console



**/api/callback**

api/login -> google server OAuth2 -> api/callback

este endpoint es solicitado desde los servidores de google

desde el servidor de google reibe una solicitud de auteticacion y autorizacion de usuario

google server OAuth2 verifica que tgenga permisos, y de sedr OK redirige al usuario a api/callback

en api/callback se recibe el usuario OK o no se llega 

si el usuario no se autentico no es posible llegar a api/callback

si se llega a api/callback quiere decir que el usuario esta autenticado y autorizado.

en api/callback se fetchea el toiken

de esta manera el usuario puede usar la app sin id explicita

pude acceder a recursos de google con ese token fetcheado

ver si en api/callback hayque guardar el token, etc



**/api/logout**

endpoint que se dispara/solicita al apretar el boton de logot

este endpoint se encarga de revocar las credenciales

y hacer una salida segura



**/protected**

seccion protegida

solo accesible por usuarios autorizados