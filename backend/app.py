import os
import datetime

from flask import Flask, session, abort, redirect, request, url_for, jsonify, make_response

from google.auth.transport import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.oauth2.credentials

import requests as rq

import logging

logging.basicConfig(level=logging.INFO)


CLIENT_SECRET_FILE = '/run/secrets/client_secret'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app = Flask("Google Login")

app.secret_key = "queonda"



## flujo de autenticacion OAuth2
flow = Flow.from_client_secrets_file(
    client_secrets_file=CLIENT_SECRET_FILE,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", 
            "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1:80/api/callback"
)



def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}




### APIs 

@app.route("/")
def home():
    return "Hola Capo <a href='/api/login'><button>Login</button></a>"


@app.route("/api/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/api/callback", methods=['GET'])
def callback():
    state = session.get("state")
    received_state = request.args.get("state")
    if state != received_state:
        return jsonify({"message": "Error: El estado de la sesión no coincide."}), 500

    code = request.args.get("code")

    if not code:
        return jsonify({"message": "Error: Falta el parámetro 'code'."}), 500

    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials
    
    session['credentials'] = credentials_to_dict(credentials)
    
    # Obtén el token de la sesión
    #credentials = flow.credentials
    access_token = credentials.token
    
    # Redirige al usuario a /api/protected con el token en el encabezado de autorización
    #response = make_response(redirect(url_for('protected')))
    #response.headers['Authorization'] = f'Bearer {access_token}'
    
    #response = make_response(redirect(url_for('protected', access_token=access_token)))
    #return response

    redirect_url = "/api/protected?access_token=" + access_token
    response = make_response(redirect(redirect_url))
    return response

    #return response
    # Redirige al usuario a /api/protected con el token en el encabezado de autorización
    #return redirect(url_for('protected'), code=302, headers={'Authorization': f'Bearer {access_token}'})
    #return redirect(url_for('protected'))




@app.route("/api/logout")
def logout():
    # Revoca Google access token
    credentials = flow.credentials
    if credentials and credentials.token:
        revoke_token_url = "https://accounts.google.com/o/oauth2/revoke"
        post_data = {"token": credentials.token}
        rq.post(revoke_token_url, data=post_data)

    session.clear()
    return redirect("/")




@app.route("/api/protected")
def protected():
    # Verifica si las credenciales están en la sesión
    if 'credentials' not in session:
        confite_content = ("<p>Que flashas confite? Logueate si queres acceder a contenido protegido</p>"
                            "<p><a href='/api/login'><button>Login</button></a></p>")
        return confite_content

    # Carga las credenciales desde la sesión
    credentials_dict = session['credentials']
    credentials_obj = google.oauth2.credentials.Credentials(**credentials_dict)

    # Asegúrate de que las credenciales sean válidas y no hayan expirado
    if not credentials_obj.valid:
        return jsonify({"error": "Credenciales inválidas o expiradas"}), 401

    
    response_content = (
        "<p>Credenciales:</p>"
        f"<pre>{credentials_dict}</pre>"
        "<p><a href='/api/logout'><button>Cerrar sesión</button></a></p>"
    )

    return response_content




@app.route("/auth", methods=['POST'])
def auth():
    #logging.debug("no lo puedo cre. estoy en /auth haciendo un POST!")
    logging.info("que onda /auth ?")
    #logging.info(f"Token recibido en /auth: {access_token}")

    # Obtener el token de acceso del parámetro de la URL
    access_token = request.args.get("access_token")
    logging.info(access_token)    
    
    if not access_token:
        return jsonify({"error": "Token de acceso no proporcionado"}), 401

    # Obtener el token de acceso del encabezado Authorization
    auth_header = request.headers.get("Authorization")
    
    logging.info(auth_header)
    logging.info('\n')

    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Token de acceso no proporcionado"}), 401

    access_token = auth_header.split(" ")[1]
    
    logging.info(access_token)
    logging.info('\n')
    
    try:
        # Verificar y decodificar el token de acceso utilizando la biblioteca google.auth
        id_info = id_token.verify_oauth2_token(
            access_token,
            requests.Request(),
            CLIENT_SECRET_FILE  # Puedes cargar esta información de forma segura como en el ejemplo anterior
        )

        # Aquí puedes realizar acciones adicionales, como verificar roles, permisos, etc.
        # También puedes almacenar información del usuario en la base de datos o en la sesión de Flask si es necesario.

        return jsonify({"message": "Autorizado", "user_info": id_info}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 401


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)