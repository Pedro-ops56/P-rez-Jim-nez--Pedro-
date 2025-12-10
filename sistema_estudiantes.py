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

# Funcion para mostrar la lista completa de estudiantes
def mostrar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes en la lista.")
        return
    
    print("Lista de Estudiantes:")
    for est in lista_estudiantes:
        print(f"{est['nombre']} {est['apellido']} - Promedio: {est['promedio']}")

# Funcion para buscar un estudiante por nombre
def buscar_estudiante(lista_estudiantes):
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    encontrados = [est for est in lista_estudiantes if est['nombre'].lower() == nombre_buscar.lower()]

    if encontrados:
        for est in encontrados:
            print(f"Encontrado: {est['nombre']} {est['apellido']} con promedio {est['promedio']}")
    else:
        print("Estudiante no encontrado.")

# Funcion para eliminar un estudiante por nombre
def eliminar_estudiante(lista_estudiantes):
    nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    inicial_len = len(lista_estudiantes)
    lista_estudiantes[:] = [est for est in lista_estudiantes if est['nombre'].lower() != nombre_eliminar.lower()]

    if len(lista_estudiantes) < inicial_len:
        print(f"Estudiante(s) con nombre {nombre_eliminar} eliminado(s) exitosamente.")
    else:
        print("Estudiante no encontrado.")

# Funcion principal del sistema
def main():
    lista_estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_estudiante(lista_estudiantes)
        elif opcion == '2':
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == '3':
            buscar_estudiante(lista_estudiantes)
        elif opcion == '4':
            eliminar_estudiante(lista_estudiantes)
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()