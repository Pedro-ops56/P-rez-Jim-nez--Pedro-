# Haz un programa que pida dos numeros y muestre si el primero es mayor, menor o igual al segundo

num1 = int(input("Ingresa el primer numero"))
num2 = int(input("Ingresa el segundo numero"))

resultado = (num1 < num2) or (num1 > num2) or (num1 == num2)
print(f'¿el primer numero es mayor, menor o igual que el segundo? {resultado}')