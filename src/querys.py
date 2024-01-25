import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("jsonFiles/secretAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def advise_of_delete():

    print("Attention, You are going to delete your Delivery, are you sure?")
    print("1. i WANT to delete")
    print("2. im not sure, plese get me out of here ")

    options = int(input("Select carefully: "))

    if options == 1 :
        return 0
    if options == 2 :
        return 1

def check_stayOrGo():

    option = input("\n Do you want do other operations? \n 1. Yes \n 2. NO \n")
    
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

def update_Data():

    id = int(input("You are going to change your name, send us your tracknumber: \n"))
    results = db.collection('TrackPackageInc').where('id', '==', id).get()

    for result in results:
        if result.exists:
            name = input("Now tell us your new name: ")
            db.collection('TrackPackageInc').document(result.id).update({'name': name})
        else:
            print(" track number not found in database")

    return check_stayOrGo()

def delete_Data():    
    
    check_point = advise_of_delete()

    if check_point == 0 :
        id = input("Insert your track number: ")

        db.collection('TrackPackageInc').where('id', '==', id).get()            
        db.collection('TrackPackageInc').document(id).delete()

        print("Your delivery was Deleted")

        return check_stayOrGo()
    
    if check_point == 1:
        return check_stayOrGo()