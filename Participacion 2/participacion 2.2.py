# Haz un programa en Python que pida al usuario ingresar un número, y muestre su tabla de multiplicar del 1 al 20, pero solo para los múltiplos pares (Es decir, numero x 2, número x 4, número x 6, etc).

numero_usuario = int(input("Ingrese un numero"))
print(f"Tabla de multiplicar {numero_usuario}:")
for i in range(0, 21, 2):
    resultado = numero_usuario * i
    print(f'{numero_usuario} x {i} = {resultado}')