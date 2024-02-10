import os
import datetime

from flask import Flask, session, abort, redirect, request, url_for, jsonify

from google.auth.transport import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.oauth2.credentials

import requests as rq

import logging

#logging.basicConfig(level=logging.DEBUG)


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
    redirect_uri="http://127.0.0.1:5000/api/callback"
)



def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}




### API Auth

@app.route("/")
def home():
    return "Hola Capo <a href='/api/login'><button>Loging</button></a>"


@app.route("/api/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    logging.debug("/api/login")
    logging.debug(authorization_url)
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

    return redirect(url_for('protected'))




@app.route("/api/logout")
def logout():
    session_id = session.get("session_id")

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
    access_token = session.get("credentials", {}).get("token")
    # mostrar algo protegido

    return "Contenido protegido. <a href='/api/logout'><button>Cerrar sesión</button></a>"



@app.route('/test')
def test_api_request():
    if 'credentials' not in session:
        return jsonify("logueate o raja de aca")#redirect('authorize')

    credentials = session['credentials']

    return jsonify(credentials)


# endpoints para listar files de google drive, guardar algo en el google drive?

# endpoint para acceder a localizacion, a info de ghoogle.
    



if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)