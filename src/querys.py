import firebase_admin
from firebase_admin import firestore

firebase_admin.initialize_app()

def insert_data():   
    

    db = firestore.client()

    insert_values = {
       "track_number": 12345124532632
    }
    
    try:
        doc_ref = db.collection("collection_name").add(insert_values)
        msg = f"Document added with ID: {doc_ref.id}"
    except Exception as e:
        msg = f"Error inserting data: {str(e)}"

    return msg
    

    

