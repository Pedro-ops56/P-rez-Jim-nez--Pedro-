# Haz un programa que pida el nombre de un contacto y su teléfono, y los agregue a un diccionario.
contactos = {}
while True:
    nombre = input("Ingrese el nombre del contacto (o 'Salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    telefono = input("Ingrese el teléfono del contacto: ")
    contactos[nombre] = telefono
print("Contactos guardados:")
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")
# --- IGNORE ---