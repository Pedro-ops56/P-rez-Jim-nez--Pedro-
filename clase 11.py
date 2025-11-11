# Ejercicio 3: Pide 6 nombres y muestra la lista numerada (1. Nombre1, 2. Nombre2, etc.)
lista_nombres = []  
for i in range(6):
    nombre = input("Ingresa un nombre: ")
    lista_nombres.append(nombre)

lista_nombres.sort()  

for i, nombre in enumerate(lista_nombres, start=1):
    print(f"{i}. {nombre}")
print("---------------------")

# Ejercicio 4: Pide 8 numeros, elimina las repeticiones y muestra la lista sin duplicados ordenados de menor a mayor.
lista_numeros = []

for i in range(8):
    numero = int(input("Introduce un numero: "))
    lista_numeros.append(numero)

lista_numeros_ordenados = list(set(lista_numeros))
lista_numeros_ordenados.sort()
print(lista_numeros_ordenados)
print("---------------------")

# Ejercicio 5: Pide 10 calificaciones entre 0 y 10. Si alguna es menor que 6, añade al conteo de reprobados. Al final muestra cuantos aprobaron y cuantos reprobaron.
lista_aprobados = []
lista_reprobados = []

for i in range(10):
    calificacion = float(input("Introduce una calificacion entre 0 y 10: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input("Calificacion invalida. Introduce una calificacion entre 0 y 10: "))
    if calificacion >= 6:
        lista_reprobados.append(calificacion)
    else:
        lista_aprobados.append(calificacion)

print(f"Cantidad de aprobados: {len(lista_aprobados)}")
print(f"Cantidad de reprobados: {len(lista_reprobados)}")
print("---------------------")

# Diccionarios en python
# nombre : "Mario"

diccionario = {
    "nombre": "Mario", 
    "apellido": "Lopez", 
    "edad": 30, 
    "licenciatura": "Ingeniero en sistemas Computacionales",
    "isEmpleado": True 
}

print(diccionario.keys()) # Devuelve las llaves del diccionario
print(diccionario.values()) # Devuelve los valores del diccionario
print(diccionario.items()) # Devuelve los pares llave-valor del diccionario
print(diccionario["nombre"]) # Muestra el valor de la llave "nombre"
print(diccionario.pop("edad")) # Elimina la llave "edad" y su valor del diccionario
print(diccionario)
len(diccionario) # Muestra la cantidad de elementos en el diccionario
print(len(diccionario))

diccionario["edad"] = 31 # Agregar o actualizar un valor en el diccionario
print(diccionario)

# Recorrer un diccionario
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

# Ejercicio 1: Crea un diccionario vacio. Pide nombres y calificaciones de 5 alumnos y guardalos en el diccionario. Luego muestra su promedio.
diccionario_alumnos = {}
for i in range(5):
    nombre = input("Ingresa el nombre del alumno: ")
    calificacion = float(input(f"Ingresa la calificacion de {nombre}: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input("Calificacion invalida. Introduce una calificacion entre 0 y 10: "))
    diccionario_alumnos[nombre] = calificacion

print(diccionario_alumnos)

for clave, valor in diccionario_alumnos.items():
    print(f"La calificacion de {clave} es: {valor}")

suma_calificaciones = sum(diccionario_alumnos.values())
promedio = suma_calificaciones / len(diccionario_alumnos)
print(f"El promedio de las calificaciones es: {promedio}")
print("---------------------")

# Ejercicio 2: Crea un diccionario con 5 productos y sus precios. Pide un producto y muestra su precio.
