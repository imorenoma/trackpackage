import os
# from dotenv import load_dotenv
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


def auth_cred():    

    cred = credentials.Certificate(
        {
            "type": "service_account",
            'project_id': PROJECT_ID,
            'private_key_id': PRIVATE_KEY_ID,
            'private_key': PRIVATE_KEY,
            'client_email': CLIENT_EMAIL,
            'client_id': CLIENT_ID,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": CLIEN_X509_CERT_URL,
            "universe_domain": "googleapis.com"
        }
    )
    return cred

def insert_data(load_cred):   
    
    # cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(load_cred)
    

    db = firestore.client()

    insert_values = {
       "track_number": 12345124532632
    }
    
    try:
        doc_ref = db.collection("package").add(insert_values)
        msg = f"Document added with ID: {doc_ref.id}"
    except Exception as e:
        msg = f"Error inserting data: {str(e)}"

    return msg

load_dotenv()

# AUTH ENV VAR

PROJECT_ID = os.environ.getenv('FIREBASE_PROJECT_ID')
PRIVATE_KEY_ID = os.environ.getenv('FIREBASE_PRIVATE_KEY_ID')
PRIVATE_KEY = os.environ.getenv('FIREBASE_PRIVATE_KEY_ID').replace('\\n', '\n') 
CLIENT_EMAIL = os.environ.getenv('FIREBASE_CLIENT_EMAIL')
CLIENT_ID =  os.environ.getenv('FIREBASE_CLIENT_ID')
CLIEN_X509_CERT_URL = os.environ.getenv('FIREBASE_CLIENT_X509_CERT_URL')
    
load_cred = auth_cred()
    

