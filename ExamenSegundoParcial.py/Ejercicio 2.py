# Pide una palabra y reemplaza todas las vocales por el simbolo '*'.
palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
palabra_modificada = "*"
for letra in palabra:
    if letra in vocales:
        palabra_modificada += "*"
    else:
        palabra_modificada += letra
print("Palabra modificada:", palabra_modificada)