from dotenv import load_dotenv
import os
import json

load_dotenv()

def key():

    PROJECT_ID = os.environ.get('FIREBASE_PROJECT_ID')
    PRIVATE_KEY_ID = os.environ.get('FIREBASE_PRIVATE_KEY_ID')
    PRIVATE_KEY = os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n','\n')
    CLIENT_MAIL = os.environ.get('FIREBASE_CLIENT_EMAIL')
    CLIENT_ID = os.environ.get('FIREBASE_CLIENT_ID')
    CLIEN_X59_CERT_URL = os.environ.get ('FIREBASE_CLIENT_X509_CERT_URL')

    my_json ={
        "type": "service_account",
        "project_id": PROJECT_ID,
        "private_key_id": PRIVATE_KEY_ID,
        "private_key":  PRIVATE_KEY,
        "client_email": CLIENT_MAIL,
        "client_id": CLIENT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": CLIEN_X59_CERT_URL,
        "universe_domain": "googleapis.com"
    }
    

    my_json = json.dumps(my_json, indent=4)

    

    with open("jsonFiles/keyJson.json", 'w') as f:
        f.write(my_json)
        f.write('\n')

key()