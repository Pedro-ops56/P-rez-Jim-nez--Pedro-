# Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece.
texto = input("Ingrese un texto: ")
palabra = input("Ingrese una palabra a buscar: ")
palabras = texto.split()
contador = palabras.count(palabra)
if contador > 0:
    print(f"La palabra '{palabra}' aparece {contador} veces.")
else:
    print(f"La palabra '{palabra}' no se encuentra en el texto.")
    
# --- IGNORE ---