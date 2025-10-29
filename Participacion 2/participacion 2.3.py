# Haz un programa que pida 5 números de los 5 números ingresados, muestra cuántos fueron mayores que 10.

num1 = float(input("Ingrese el primer numero"))
num2 = float(input("Ingrese el segundo numero"))
num3 = float(input("Ingrese el tercer numero"))
num4 = float(input("Ingrese el cuarto numero"))
num5 = float(input("Ingrese el quinto numero"))
contador_mayoresde10 = 0
if num1 >10:
    contador_mayoresde10 += 1
if num2 >10:
    contador_mayoresde10 += 1
if num3 >10:
    contador_mayoresde10 += 1
if num4 >10:
    contador_mayoresde10 += 1
if num5 >10:
    contador_mayoresde10 += 1
print(f"numeros mayores a 10: {contador_mayoresde10}")