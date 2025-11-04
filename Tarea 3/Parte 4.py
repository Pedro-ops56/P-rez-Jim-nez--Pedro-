# Haz un programa que sume todos los números impares del 1 al 50.
suma_impares = 0
for numero in range(1, 51):
    if numero % 2 != 0:
        suma_impares += numero
print(f"La suma de los numeros impares del 1 al 50 es: {suma_impares}")