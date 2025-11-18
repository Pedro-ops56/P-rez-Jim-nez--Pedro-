# Sistema de Gestion de Estudiantes

# Funcion para mostrar las opciones del menu
def mostrar_menu():
    print("Sistema de Gestion de Estudiantes")
    print("1. Agregar Estudiante")
    print("2. Mostrar lista completa de Estudiantes")
    print("3. Buscar Estudiante por nombre")
    print("4. Eliminar Estudiante")
    print("5. Salir")

# Funcion para agregar un estudiante a la lista
def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))

    lista_estudiantes.append({'nombre': nombre, 'apellido': apellido, 'promedio': promedio})

    print(f"Estudiante {nombre} {apellido} agregado exitosamente.")

# Mostrar menu funciones