palabra = "Palabra de ejemplo"

for letra in palabra:
    print(letra)

# Ejercicio 3: Haz un programa que pida nombre y apellido. Muestra en pantalla en formato Apeelido, Nombre con cada palabra iniciando con mayuscula.
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nombre_completo = apellido + ", " + nombre

print(f"{apellido.capitalize()}, {nombre.capitalize()}")
print(nombre_completo.title())