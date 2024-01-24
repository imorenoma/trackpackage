import os
# from dotenv import load_dotenv
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

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


def app_cred():

    const firebaseConfig = {
        apiKey: "AIzaSyBw5uCo5X3lEx0KpKmU6xnUgS9f2pHNY2g",
        authDomain: "trackerapp-9a5d0.firebaseapp.com",
        projectId: "trackerapp-9a5d0",
        storageBucket: "trackerapp-9a5d0.appspot.com",
        messagingSenderId: "64206924966",
        appId: "1:64206924966:web:fb769208690b3cbb819867",
        measurementId: "G-869E2KSZTZ"
    };
    
    const app = initializeApp(firebaseConfig);
    const analytics = getAnalytics(app);

    return firebaseConfig


def insert_data(load_cred):   
    
    # cred = credentials.ApplicationDefault()
    # firebase_admin.initialize_app(load_cred)
    
    

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

PROJECT_ID = os.getenv('FIREBASE_PROJECT_ID')
PRIVATE_KEY_ID = os.getenv('FIREBASE_PRIVATE_KEY_ID')
PRIVATE_KEY = os.getenv('FIREBASE_PRIVATE_KEY_ID').replace('\\n', '\n') 
CLIENT_EMAIL = os.getenv('FIREBASE_CLIENT_EMAIL')
CLIENT_ID =  os.getenv('FIREBASE_CLIENT_ID')
CLIEN_X509_CERT_URL = os.getenv('FIREBASE_CLIENT_X509_CERT_URL')
    
load_cred = auth_cred()
    

