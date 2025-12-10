# funciones en Python

# Definicion de una funcion
def saludar():
    print("Hola, bienvenido a la clase de Python.")

# Llamada a la funcion sin argumentos
def saludar():
    print("Hola, ¿cómo estás?")


# Funcion con parametros por defecto
def saludar_persona(nombre, apellido, edad):
    print(f"Hola {nombre} {apellido}, tienes {edad} años.")

# Llamada a la funcion con argumentos
saludar_persona("Ana", "Gomez", 25)
saludar_persona("Luis", "Martinez", 30)
saludar_persona("Carla", "Ramirez", 22)

# Funcion con valor retorno
def sumar(a, b):
    return a + b

print(sumar(5, 10))
resultado = sumar(15, 25)
print("El resultado de la suma es:", resultado)