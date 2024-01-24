import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("secretAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()


def menu():
    print("Bienvenido a TrackPackage. Elige una opción")
    while True:
        print("1. Create registry")
        print("2. Read database ")
        print("3. Read by id ")
        print("4. Update by id")
        print("5. Delete database")
        print("0. Salir")

        opcion = int(input("Ingresa tu peticion: "))

        if opcion == 0:
            print("seeya")
            break
        
        elif opcion == 1:
            id = int(input("Ingresa id del package: "))

            name = input(("Ingresa tu nombre: "))
            premium = bool(input("Eres premium (True/False): ").lower())
            db.collection('TrackPackageInc').document(str(id)).set({'id': id, 'name': name, 'premium': premium})        
            #db.collection('TrackPackageInc').document(str(id)).add({'id': id, 'name': name, 'premium': premium})
            opcion = int(input("\n Deseas continuar? \n 1. SI \n 2. NO \n"))
            if opcion == 2:
                break
            else:
                continue

        elif opcion == 2:
            document = input("Inserta el nº de documento: \n")
            result = db.collection('TrackPackageInc').document(document).get()
            if result.exists:
                print(result.to_dict())
                opcion = int(input("\n Deseas continuar? \n 1. SI \n 2. NO \n"))
            if opcion == 2:
                break
            else:
                continue

        elif opcion == 3:
            id = int(input("\n Dame el id de tu pedido: \n"))
            results = db.collection('TrackPackageInc').where('id', '==', id).get()
            for result in results:
                print("\n" + result.to_dict() + "\n")
                opcion = int(input("\n Deseas continuar? \n 1. SI \n 2. NO \n"))
            if opcion == 2:
                break
            else:
                continue

        elif opcion == 4:
             id = int(input("Vas a cambiar tu nombre, indica el id de tu pedido: \n"))
             results = db.collection('TrackPackageInc').where('id', '==', id).get()
             for result in results:
                if result.exists:
                    name = input("Ahora indica cual sera el nuevo nombre: \n")
                    db.collection('TrackPackageInc').document(result.id).update({'name': name})
                else:
                    print("Opcion no valida")
                    break
             opcion = int(input("\n Deseas continuar? \n 1. SI \n 2. NO \n"))
             if opcion == 2:
                break
             else:
                continue

        elif opcion == 5: 
            id = input("Inserta el nº de id que deseas eliminar: \n")

            results = db.collection('TrackPackageInc').where('id', '==', id).get()            
            db.collection('TrackPackageInc').document(id).delete()
           

        else:
            print("Opción no válida. Por favor, ingresa un número del 0 al 5.")

menu()


#CREATE
# db.collection('TrackPackageInc').add({'id': 234824, 'name': "Pepe", 'premium': True})
# db.collection('TrackPackageInc').add({'id': 6565756, 'name': "Stuart", 'premium': False})
# db.collection('TrackPackageInc').add({'id': 34541, 'name': "Luis", 'premium': True})

# #READ
# result = db.collection('TrackPackageInc').document('71NUc0uudmslnQb9YrnM').get()

# if result.exists:
#     print(result.to_dict())

    #READ ALL

# docs = db.collection('TrackPackageInc').get()
# for doc in docs:
#     print(doc.to_dict())


# db.collection('TrackPackageInc').get({'id': 6565756, 'name': "Stuart", 'premium': False})
# db.collection('TrackPackageInc').get({'id': 34541, 'name': "Luis", 'premium': True})

# #UPDATE
# db.collection('TrackPackageInc').update({'id': 234824, 'name': "Pepe", 'premium': True})
# db.collection('TrackPackageInc').update({'id': 6565756, 'name': "Stuart", 'premium': False})
# db.collection('TrackPackageInc').update({'id': 34541, 'name': "Luis", 'premium': True})

# #DELETE
# db.collection('TrackPackageInc').delete({'id': 234824, 'name': "Pepe", 'premium': True})
# db.collection('TrackPackageInc').delete({'id': 6565756, 'name': "Stuart", 'premium': False})
# db.collection('TrackPackageInc').delete({'id': 34541, 'name': "Luis", 'premium': True})

# print("Elige que quieres hacer: ")


# choice = input()

# if 0 <= choice <= 10:
#     while choice != 0:
#         if choice == 1:
#             db.collection('TrackPackageInc').document('packages').add({'id': 234824, 'name': "Pepe", 'premium': True})

            
