# Importar las librerías necesarias
import firebase_admin
from firebase_admin import firestore

# Crear una conexión a Firebase
firebase_admin.initialize_app()

# Crear la colección de envíos
db = firestore.Client()
envios_col = db.collection("envios")

# Función para crear un envío
def crear_envio():
    # Solicitar los datos del envío
    remitente = input("Remitente: ")
    destinatario = input("Destinatario: ")
    paquete = input("Paquete: ")
    fecha_envio = input("Fecha de envío: ")
    fecha_entrega = input("Fecha de entrega: ")

    # Crear un documento para el envío
    envio = {
        "remitente": remitente,
        "destinatario": destinatario,
        "paquete": paquete,
        "fecha_envio": fecha_envio,
        "fecha_entrega": fecha_entrega,
        "estado": 1
    }

    # Guardar el documento en la colección
    envios_col.add(envio)

# Función para actualizar el estado de un envío
def actualizar_estado():
    # Solicitar el ID del envío
    id_envio = input("ID del envío: ")

    # Solicitar el nuevo estado
    nuevo_estado = int(input("Nuevo estado (1-creado, 2-en tránsito, 0-entregado): "))

    # Actualizar el estado del documento
    envios_col.document(id_envio).update({"estado": nuevo_estado})

# Función para borrar un envío
def borrar_envio():
    # Solicitar el ID del envío
    id_envio = input("ID del envío: ")

    # Borrar el documento
    envios_col.document(id_envio).delete()

# Función para editar un envío
def editar_envio():
    # Solicitar el ID del envío
    id_envio = input("ID del envío: ")

    # Solicitar los datos a editar
    campo = input("Campo a editar: ")
    nuevo_valor = input("Nuevo valor: ")

    # Editar el documento
    envios_col.document(id_envio).update({campo: nuevo_valor})

# Función para editar la fecha de entrega de un envío
def editar_fecha_entrega():
    # Solicitar el ID del envío
    id_envio = input("ID del envío: ")

    # Solicitar la nueva fecha de entrega
    nueva_fecha_entrega = input("Nueva fecha de entrega: ")

    # Editar el documento
    envios_col.document(id_envio).update({"fecha_entrega": nueva_fecha_entrega})

# Función para consultar un envío individual
def consultar_envio():
    # Solicitar el ID del envío
    id_envio = input("ID del envío: ")
    # Consultar el documento
    envio = envios_col.document(id_envio).get()

def listar_envios():
    # Obtener todos los envíos de la colección
    envios = envios_col.get()

    # Imprimir los datos de los envíos
    for envio in envios:
        print("ID del envío:", envio.id)
        print("Remitente:", envio.get("remitente"))
        print("Destinatario:", envio.get("destinatario"))
        print("Paquete:", envio.get("paquete"))
        print("Fecha de envío:", envio.get("fecha_envio"))
        print("Fecha de entrega:", envio.get("fecha_entrega"))
        print("Estado:", envio.get("estado"))