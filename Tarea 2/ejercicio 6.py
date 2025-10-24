#Haz un programa que pida tres números y muestre si se cumple la expresión A < B < C (solo mostrando el resultado lógico).

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

resultado = num1 < num2 < num3

print(f"¿Se cumple la expresion A < B < C? {resultado}")