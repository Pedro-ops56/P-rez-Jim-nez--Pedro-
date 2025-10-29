# for variable in iterable:
#     bloque de código


# funcion range(incio, fin, paso)

# Ejemplo usando range, se imprimiran todos los pares del 0 al 10
for i in range(0, 11, 2):
    print(i)

# Ejercicio 1: Haz un programa que muestre los numeros del 1 al 20
print("Numeros del 1 al 20")
for numero in range(1, 21):
    print(numero)

print("-------------------------------")

# Ejercicio 2: Haz un programa que muestre la tabla de multiplicar de un numero dado por el usuario (del 1 al 10)

numero_usuario =int(input("Introduce un numero: "))
print(f"Tabla de multiplicar del {numero_usuario}: ")
for i in range(1, 11):
    resultado = numero_usuario * i
    print(f'{numero_usuario} x {i} = {resultado}')