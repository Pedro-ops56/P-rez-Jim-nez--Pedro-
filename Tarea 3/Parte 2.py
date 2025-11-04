# Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo.
positivos = 0
negativos = 0
numero = 1  # Inicializamos con un valor distinto de cero para entrar al bucle
while numero != 0:
    numero = float(input("Ingresa un numero (0 es el final)"))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Numeros positivos ingresados: {positivos}")
print(f"Numeros negativos ingresados: {negativos}")