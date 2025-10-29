# Haz un programa en Python que pida un número, posteriormente muestra todos los números desde 1 hasta el número ingresando. Imprime en consola un coteo de números pares y de números impares.

numero = int(input("Ingresa un numero"))
contador_pares = 0
contador_impares = 0

for i in range(1, numero + 1):
    print(i)
    if i % 2 ==0:
        contador_pares += 1
    else:
        contador_impares += 1
print(f"numeros pares: {contador_pares}")
print(f"numeros impares: {contador_impares}")