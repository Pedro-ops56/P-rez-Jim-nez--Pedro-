# Haz un programa que pida una frase y cuenta cuantas letras tiene la frase sin contar espacios.
frase = input("Ingresa una frase: ")
frase_sin_espacios = frase.replace(" ", "")
cantidad_letras = len(frase_sin_espacios)
print(f"La cantidad de letras sin contar espacios es: {cantidad_letras}")