# Haz un programa que pida tres números y muestre si los tres son iguales (solo mostrando True o False).

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

resultado = num1 == num2 == num3

print(f"¿Los tres numeros son iguales? {resultado}")