# Crea un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar un campo de gimnasio.
from tabulate import tabulate

def menu():
    print("----- Gestión de Campos de Gimnasio -----")
    print("1. Agregar registro de Campo gimnasio")
    print("2. Consultar registro de Campo gimnasio")
    print("3. Actualizar registro de Campo gimnasio")
    print("4. Eliminar registro de Campo gimnasio")
    print("5. Salir")

# Creacion del registro
import json
diccionario_campos = {}
while True:
    menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == '1':
        id_campo = input("Ingresa el ID del Campo gimnasio: ")
        nombre = input("Ingresa el nombre del Campo gimnasio: ")
        ubicacion = input("Ingresa la ubicación del Campo gimnasio: ")
        estado = input("Ingresa el estado del Campo gimnasio: ")
        capacidad = input("Ingresa la capacidad del Campo gimnasio: ")
        diccionario_campos[id_campo] = {
            "Nombre": nombre,
            "Ubicación": ubicacion,
            "Estado": estado,
            "Capacidad": capacidad
        }
        print("Registro agregado exitosamente.")
        import json
        datos_json = json.dumps(diccionario_campos, indent=4)
        with open("campos_gimnasio.json", "w") as archivo_json:
            archivo_json.write(datos_json)
    
    elif opcion == '2':
        id_campo = input("Ingresa el ID del Campo gimnasio a consultar: ")
        if id_campo in diccionario_campos:
            print(f"Registro del Campo gimnasio {id_campo}: {diccionario_campos[id_campo]}")
        else:
            print("El registro no existe.")
            
    elif opcion == '3':
        id_campo = input("Ingresa el ID del Campo gimnasio a actualizar: ")
        if id_campo in diccionario_campos:
            nombre = input("Ingresa el nuevo nombre del Campo gimnasio: ")
            ubicacion = input("Ingresa la nueva ubicación del Campo gimnasio: ")
            estado = input("Ingresa el nuevo estado del Campo gimnasio: ")
            capacidad = input("Ingresa la nueva capacidad del Campo gimnasio: ")
            diccionario_campos[id_campo] = {
                "Nombre": nombre,
                "Ubicación": ubicacion,
                "Estado": estado,
                "Capacidad": capacidad
            }
            print("Registro actualizado exitosamente.")
        else:
            print("El registro no existe.")
    
    elif opcion == '4':
        id_campo = input("Ingresa el ID del Campo gimnasio a eliminar: ")
        if id_campo in diccionario_campos:
            del diccionario_campos[id_campo]
            print("Registro eliminado exitosamente.")
        else:
            print("El registro no existe.")
    
    elif opcion == '5':
        print("Saliendo del sistema de gestión de Campos de Gimnasio.")
        break
    
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

# Lectura o consulta de registros
print("Registros actuales de Campos de Gimnasio:")
for id_campo, detalles in diccionario_campos.items():
    print(f"ID: {id_campo}, Detalles: {detalles}")
headers = ["ID", "Nombre", "Ubicación", "Estado", "Capacidad"]
with open("campos_gimnasio.csv", "w") as archivo:
    archivo.write(",".join(headers) + "\n")
    for id_campo, detalles in diccionario_campos.items():
        linea = f"{id_campo},{detalles['Nombre']},{detalles['Ubicación']},{detalles['Estado']},{detalles['Capacidad']}\n"
        archivo.write(linea)
print("Registros guardados en 'campos_gimnasio.csv'.")

# Actualizacion o modificacion de registros
with open("campos_gimnasio.json", "w") as archivo_json:
    json.dump(diccionario_campos, archivo_json, indent=4)
print("Registros guardados en 'campos_gimnasio.json'.")
id_campo = input("Ingresa el ID del Campo gimnasio a actualizar en el archivo JSON: ")
if id_campo in diccionario_campos:
    nombre = input("Ingresa el nuevo nombre del Campo gimnasio: ")
    ubicacion = input("Ingresa la nueva ubicación del Campo gimnasio: ")
    estado = input("Ingresa el nuevo estado del Campo gimnasio: ")
    capacidad = input("Ingresa la nueva capacidad del Campo gimnasio: ")
    diccionario_campos[id_campo] = {
        "Nombre": nombre,
        "Ubicación": ubicacion,
        "Estado": estado,
        "Capacidad": capacidad
    }
    with open("campos_gimnasio.json", "w") as archivo_json:
        json.dump(diccionario_campos, archivo_json, indent=4)
    print("Registro actualizado en 'campos_gimnasio.json'.")

# Eliminacion de registros
def confirmar(mensaje="¿Estás seguro? (s/n): "):
    respuesta = input(mensaje).lower()
    return respuesta == 's'
id_campo = input("Ingresa el ID del Campo gimnasio a eliminar del archivo JSON: ")
if id_campo in diccionario_campos:
    if confirmar("¿Estás seguro de que deseas eliminar este registro? (s/n): "):
        del diccionario_campos[id_campo]
        with open("campos_gimnasio.json", "w") as archivo_json:
            json.dump(diccionario_campos, archivo_json, indent=4)
        print("Registro eliminado de 'campos_gimnasio.json'.")
    else:
        print("Eliminación cancelada.")
else:
    print("El registro no existe en el archivo JSON.")

# Archivo README.txt
with open("README.txt", "w") as readme:
    readme.write("Sistema CRUD para Gestión de Campos de Gimnasio\n")
    readme.write("Este sistema permite crear, leer, actualizar y eliminar registros de campos de gimnasio.\n")
    readme.write("Los registros se almacenan en archivos JSON y CSV para su fácil acceso y manipulación.\n")
    readme.write("Instrucciones:\n")
    readme.write("1. Ejecuta el script para iniciar el menú de gestión.\n")
    readme.write("2. Selecciona la opción deseada para realizar operaciones CRUD.\n")
    readme.write("3. Los cambios se reflejarán en los archivos 'campos_gimnasio.json' y 'campos_gimnasio.csv'.\n")
    readme.write("Nombre del proyecto: Gestión de Campos de Gimnasio\n")
    readme.write("Integrantes: [Pedro Javier Pérez Jiménez, Ricardo Pérez, Juan]\n")
    print("Archivo README.txt creado.")