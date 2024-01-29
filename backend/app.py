import os
import dotenv
import datetime

from flask import Flask, session, abort, redirect, request, url_for
from flask_migrate import Migrate
from google.auth.transport import requests
from google.oauth2 import id_token

from google_auth_oauthlib.flow import Flow
import requests as rq

from flask_sqlalchemy import SQLAlchemy
from flask_session import Session as flask_ses

from flask import jsonify

import logging

logging.basicConfig(level=logging.DEBUG)


dotenv.load_dotenv('/env/backend.env')

#GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]#
#CLIENT_SECRET_FILE = os.environ["CLIENT_SECRET_FILE"]

# Acceder a las variables de entorno
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app = Flask("Google Login")

app.secret_key = "queonda"
# app.secret_key = os.urandom(24)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SESSION_TYPE'] = 'filesystem'


db = SQLAlchemy(app)

flask_ses(app)

migrate = Migrate(app, db)


### flujo de autenticacion OAuth
flow = Flow.from_client_secrets_file(
    client_secrets_file=CLIENT_SECRET_FILE,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1/api/callback"
)



### utilis

def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}


def get_scope_info(access_token):
    # Verificar y decodificar el access token
    id_info = id_token.verify_oauth2_token(
        access_token,
        requests.Request(),
        GOOGLE_CLIENT_ID
    )

    # Obtener los scopes del access token
    scopes = id_info.get('scope')

    # Retornar la información de los scopes
    return scopes


import json

@app.route("/api/login", methods=['GET'])
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state

    response_data = {
        "authorization_url": authorization_url
    }
    return json.dumps(response_data), 200, {'Content-Type': 'application/json'}



import jwt

@app.route("/api/callback", methods=['GET'])
def callback():
    state = session.get("state")
    received_state = request.args.get("state")
    print("Received state:", received_state)
    if state != received_state:
        return jsonify({"message": "Error: El estado de la sesión no coincide."}), 500

    code = request.args.get("code")

    if not code:
        return jsonify({"message": "Error: Falta el parámetro 'code'."}), 500


    flow.fetch_token(authorization_response=request.url)


    #logging.debug(credentials)
    # Save the credentials to the session
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    logging.debug(session['credentials'])
    # Obtener el token de acceso de las credenciales

    return redirect(url_for('protected'))




@app.route("/api/logout")
def logout():
    # Obtener el id de sesión de la sesión de Flask
    session_id = session.get("session_id")

    if session_id:
        # Buscar la sesión en la base de datos y actualizar el campo logout_time
        session_data = Session.query.get(session_id)
        if session_data:
            session_data.logout_time = datetime.datetime.now()
            db.session.commit()

    # Revoca Google access token
    credentials = flow.credentials
    if credentials and credentials.token:
        revoke_token_url = "https://accounts.google.com/o/oauth2/revoke"
        post_data = {"token": credentials.token}
        rq.post(revoke_token_url, data=post_data)

    session.clear()
    return redirect("/")



#@app.route("/api/protected")
##@login_is_required
#def protected():
#    return "Ojo... <a href='/api/logout'><button>Logout</button></a>"




from google.auth.transport import requests

def validate_access_token(token):
    try:
        logging.debug("entro aca? balastrule. probablemente aca este fallando...")
        logging.debug(token)
        id_info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID
        )
        logging.debug("solo decime si entre aca")

        # Verificar que el token sea válido y no haya expirado
        if id_info.get('aud') == GOOGLE_CLIENT_ID:
            return True
    except ValueError:
        pass
    return False


@app.route("/api/protected")
def protected():
    access_token = session.get("credentials", {}).get("token")
    if not validate_access_token(access_token):
        return abort(401)
    return "Contenido protegido. <a href='/api/logout'><button>Cerrar sesión</button></a>"


import google.oauth2.credentials
import google_auth_oauthlib.flow
#import googleapiclient.discovery

@app.route('/test')
def test_api_request():
  if 'credentials' not in session:
    return redirect('authorize')

  # Load credentials from the session.
  credentials = session['credentials']


  ## este test es sobre google drive
  #drive = googleapiclient.discovery.build(
  #    API_SERVICE_NAME, API_VERSION, credentials=credentials)

 # files = drive.files().list().execute()

  # Save credentials back to session in case access token was refreshed.
  # ACTION ITEM: In a production app, you likely want to save these
  #              credentials in a persistent database instead.
  session['credentials'] = credentials_to_dict(credentials)

  #return jsonify(**files)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=3001)
    #app.run()
