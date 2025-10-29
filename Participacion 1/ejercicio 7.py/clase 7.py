# Ejercicio 3: Haz un programa en python que pida un número entero y muestra cuántos números pares hay desde 1 hasta ese número (incluyendo si es par)

conteo_pares = 0
#Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1):
    if i % 2 == 0:
        conteo_pares += 1
    print(i)

print(f"Hay{conteo_pares} números pares desde 1 hasta {numero}.")

print("-----------------")

# Ejercicio 4: Haz un programa en python que pida un número y calcule el factorial de ese numero utilizando un ciclo for.
numero = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es {factorial}.") 

print("-------------------")

# Bucle while
# while condicion:
#     bloque de codigo

# Ejercicio 1: Haz un programa que pida al usuario una contraseña hasta que ingrese la correcta y que tenga maximo 5 intentos.

# Definir la contraseña correcta
contraseña_correcta = "Marcus"
intentos = 0
max_intentos = 5
contraseña = input("Ingrese la contraseña")
while (intentos < max_intentos) or (contraseña != contraseña_correcta):
    print("Contraseña incorrecta. Intenta de nuevo. ")
    intentos += 1
    contraseña = input("Ingrese la contraseña: ")

if intentos == max_intentos:
    print("Has excedido el numero maximo de intos. Acceso denegado.")
else:
    print(f"contraseña correcta: Acceso concedido. Intentos realizados{intentos}.")

print("--------------------")

# Ejercicio 2: Haz un programa que pida al usuario ingresar números positivos y que se detenga hasta que ingrese un numero negativo.

numero = float(input("Ingrese un número positivo (o un numero neegativo para salir):"))

while numero >= 0:
     numero = float(input("Ingrese un numero positivo (o un numero negatvio para salir)"))

print("Numero negatvio ingresado. Programa terminado")

print("----------------")

# Ejercicio 3: Haz un programa que sume todos los número que ingrese el usuario hasta que ingrese un 0
suma = 0
numero = float(input("Ingrese un número para sumar (o 0 para salir):"))

while numero != 0:
    suma += numero
    numero = float(input("Ingrese un numero para sumar (o 0 para salir):"))

print(f"La suma total de los numeros ingresados es: {suma}")
