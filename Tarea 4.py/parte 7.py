# Haz un programa en Python que pida repetidamente el nombre de una persona y su respuesta ("Si" o "No"). Guarda cada respuesta en un diccionario, donde la clave sea el nombre y el valor la respuesta. El programa debe terminar cuando el usuario escriba "Fin" como nombre. Al finalizar, muestra cuántas personas respondieron "Si", y cuántas respondieron "No"
respuestas = {}
while True:
    nombre = input("Ingrese el nombre de la persona (o 'Fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    respuesta = input("Ingrese la respuesta ('Si' o 'No'): ")
    respuestas[nombre] = respuesta
contador_si = sum(1 for r in respuestas.values() if r.lower() == 'si')
contador_no = sum(1 for r in respuestas.values() if r.lower() == 'no')
print(f"Cantidad de respuestas 'Si': {contador_si}")
print(f"Cantidad de respuestas 'No': {contador_no}")