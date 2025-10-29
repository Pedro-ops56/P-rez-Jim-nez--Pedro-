# Haz un programa que sume todos los números pares del 1 al 100. Al final muestra el resultado de la suma.

suma_pares = 0
for i in range(1, 101, 2):
    suma_pares += i
print(f"La suma de los numeros pares es {suma_pares}")