# Documentacion de la app

### VER

Manipulación de sesiones: 

utiliza la sesión de Flask para almacenar información como "session_id", "google_id" y "name". 
tomar las precauciones necesarias para proteger la sesión y evitar ataques de secuestro de sesión:
    . configurar un secret key fuerte  
    . asegurarte de que la sesión se almacene de manera segura. 

información sobre las mejores prácticas de manejo de sesiones en la documentación de Flask



#### comportamiento de la app

cuado se crea el microserviio db se crea el volumen db_data pero consolo con la configuracion

el problema es que arranca la app pero no reconoce la conexion con la bd -> flask db init

una vezz que reconoce la bd, hay que restartear lios servicios
ahi va a aparecer db_data/nueva_BD

ahi arrancar los servicios, entrar en app y migrar

flask db migrate

flask db upgrade

ahora si aparecen las tablas persistentes en el columen db_data


#### Refs

https://developers.google.com/identity/protocols/oauth2/web-server?hl=es-419#ios


idolo

https://www.youtube.com/watch?v=nhqcecpi47s&ab_channel=Docker



### buenas practicas de Login y Autenticacion

. Uso de tokens JWT: 
Utiliza tokens JWT (JSON Web Tokens) para autenticar y autorizar las solicitudes entre los microservicios. 
Los tokens JWT son seguros, compactos y autocontenidos, lo que los hace ideales para la comunicación entre microservicios.

. Servicio de autenticación centralizado: 
Considera implementar un servicio de autenticación centralizado que maneje la lógica de autenticación y emita tokens JWT. Esto permite que todos los microservicios confíen en este servicio centralizado para autenticar a los usuarios y validar los tokens JWT.

. Uso de HTTPS: 
Asegúrate de utilizar HTTPS en todas las comunicaciones entre los microservicios y los clientes. 
Esto ayuda a proteger la confidencialidad y la integridad de los datos durante la autenticación y la transferencia de tokens.

. Validación y verificación de tokens: 
Cada microservicio debe validar y verificar los tokens JWT recibidos para asegurarse de que sean auténticos y no hayan sido modificados. Esto implica verificar la firma del token, comprobar la validez de la fecha de expiración y asegurarse de que el token contenga los permisos necesarios para acceder a los recursos protegidos.

. Implementación de políticas de autorización: 
Además de la autenticación, asegúrate de implementar políticas de autorización en cada microservicio para controlar el acceso a los recursos protegidos. Estas políticas pueden basarse en los roles y permisos asignados a los usuarios autenticados.




### Flujo de interacción entre los microservicios:

El cliente (frontend) realiza una solicitud de inicio de sesión al microservicio de autenticación (backend).

El microservicio de autenticación valida las credenciales del usuario y genera un token JWT válido.

El microservicio de autenticación devuelve el token JWT al cliente.

El cliente incluye el token JWT en cada solicitud subsiguiente a los otros microservicios.

Cuando un microservicio recibe una solicitud con un token JWT, lo valida y verifica su autenticidad.
Si el token es válido, el microservicio procesa la solicitud y devuelve la respuesta correspondiente al cliente.


#### ejemplo del flujo de interacción en una arquitectura de microservicios:

El cliente (frontend) realiza una solicitud de inicio de sesión enviando las credenciales al microservicio de autenticación (backend).

El microservicio de autenticación valida las credenciales y genera un token JWT válido.

El microservicio de autenticación devuelve el token JWT al cliente.

El cliente incluye el token JWT en el encabezado Authorization de cada solicitud subsiguiente a los otros microservicios.

Cuando un microservicio recibe una solicitud, valida y verifica el token JWT para asegurarse de que sea auténtico y no haya sido modificado.

Si el token es válido, el microservicio procesa la solicitud y devuelve la respuesta correspondiente al cliente.
Si el token es inválido o ha expirado, el microservicio devuelve una respuesta de error al cliente, indicando que se requiere una autenticación vál


1. el frontend envia una solicitud GET al backend endpoint /api/login
2. el backend endpoint /api/login le responde al frontend un msj json con authorization_url
3. el frontend recibe la respuesta y redirige al usuario a  authorization_url con window.location.href = authorizationUrl;
4. el usuario es redirigido a google account
5. el usuario se loguea en google account
6. el usuario es redirigido desde google account al backend endpoint /api/callback
7. el backend endpoint /api/callback autentica el usuario y manda un mensaje al frontend con el nombre del usuario autenticado.

el mensaje con el nombre del usuario autenticado enviado del backend endpoint /api/callback hacia el frontend
que tipo de mensaje es?


Las buenas prácticas dictan que el backend redirige el token al frontend. Esto se debe a que el token de autenticación es una pieza sensible de información que se utiliza para verificar y autorizar las solicitudes del cliente. Al enviar el token al frontend, permite que el cliente lo almacene y lo utilice en las solicitudes subsiguientes al backend para autenticarse.

Cuando el backend autentica al usuario, en lugar de devolver directamente el token en la respuesta JSON, es recomendable redirigir al frontend a una URL específica y pasar el token como parte de la URL. Esto se hace por razones de seguridad, ya que al redirigir al frontend y pasar el token en la URL, se asegura de que el token no se exponga innecesariamente en el cuerpo de una respuesta JSON, donde podría ser interceptado o accedido por terceros no autorizados.

Una vez que el frontend recibe el token en la URL de redirección, puede almacenarlo de forma segura y utilizarlo en las solicitudes subsiguientes al backend para autenticarse. El frontend puede almacenar el token en el estado de la aplicación o en una cookie segura, dependiendo de la implementación y las necesidades específicas.

En resumen, las buenas prácticas sugieren que el backend redirija el token al frontend para que pueda ser almacenado y utilizado por el cliente de manera segura en las solicitudes subsiguientes al backend.

