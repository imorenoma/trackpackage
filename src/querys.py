import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("jsonFiles/secretAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def check_stayOrGo():

    option = input("\n Do you want to continue? \n 1. Yes \n 2. NO \n")
    
    if option == "Yes" or option == "yes" or option == "Y" or option == "y":
        option = 1
        return option
        
    if  option == "No" or option == "no" or option == "N" or option == "n":
        option = 2
        return option
    
    if option == "1" or option == "2":
        return int(option)
    

def create_Registry():

    id = int(input("Insert id of the package: "))

    name = input(("Tell us your name: " ))
    premium = bool(input("Are you Premium (True/False): ").lower())

    db.collection('TrackPackageInc').document(str(id)).set({'id': id, 'name': name, 'premium': premium})        
    
    return check_stayOrGo()

    
def check_Database():

    document = input("Insert the track number: \n")
    result = db.collection('TrackPackageInc').document(document).get()

    if result.exists:
        result_to_dict = result.to_dict()

        print("---------------------")
        for key, value in result_to_dict.items():
            print(f"{key} : {value}", '\n')
        print("---------------------")
    
    return check_stayOrGo()

