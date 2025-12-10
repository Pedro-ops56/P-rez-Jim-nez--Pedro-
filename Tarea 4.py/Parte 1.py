# Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras. Muestra la lista resultante.
def mostrar_menu():
    print("Menu de opciones:")
    print("1. Ingresar una frase")
    print("2. Salir")
def obtener_palabras_largas(frase):
    palabras = frase.split()
    palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
    return palabras_largas
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-2): ")
    if opcion == '1':
        frase = input("Ingrese una frase: ")
        resultado = obtener_palabras_largas(frase)
        print("Palabras con más de 5 letras:", resultado)
    elif opcion == '2':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
# --- IGNORE ---