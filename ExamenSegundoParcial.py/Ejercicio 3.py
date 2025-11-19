# Haz un programa que pida un numero entero N, y calcula la suma de todos los numeros del 1 al N.
numero = int(input("Ingresa un numero entero N: "))
suma = sum(range(1, numero + 1))
print(f"La suma de todos los numeros del 1 al {numero} es: {suma}")
print("Listo")