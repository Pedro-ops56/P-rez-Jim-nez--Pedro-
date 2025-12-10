# Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación). Elimina los elementos repetidos y los que sean menores a 3 letras. Muestra la nueva lista e imprímela en pantalla. 
entrada = input("Ingrese una lista de palabras separadas por comas: ")
palabras = entrada.split(",")
palabras_limpias = []
for palabra in palabras:
    palabra = palabra.strip()
    if palabra not in palabras_limpias and len(palabra) >= 3:
        palabras_limpias.append(palabra)
print("Lista limpia:", palabras_limpias)