# Haz un programa que pida una frase y cuenta cuántas veces aparece cada palabra. Por ejemplo "Esta es una prueba", "Esta" aparece una vez, "es", una vez, "una", una vez, etc...
frase = input("Ingrese una frase: ")
palabras = frase.split()
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
        
for palabra, contador in contador_palabras.items():
    print(f"La palabra '{palabra}' aparece {contador} veces.")
# --- IGNORE ---