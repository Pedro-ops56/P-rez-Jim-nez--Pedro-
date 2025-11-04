# Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7.
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    num1, num2 = num2, num1
print(f"Multiplos de 7 entre {num1} y {num2}:")
for numero in range(num1, num2 + 1):
    if numero % 7 == 0:
        print(numero)
print(f"Has ingresado los numeros: {num1} y {num2}")