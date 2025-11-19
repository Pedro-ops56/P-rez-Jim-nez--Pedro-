# Haz un programa que pida una palabra, y cuenta cuantas vocales tiene la palabra ingresada.
palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
cantidad_vocales = 0
for letra in palabra:
    if letra in vocales:
        cantidad_vocales += 1
print(f"La cantidad de vocales en la palabra es: {cantidad_vocales}")