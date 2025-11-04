# Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos.

numero = int(input("Ingrese un numero"))

if numero % 2 == 0 and numero % 3 == 0:
    print(f"El numero {numero} es divisble entre 2 y 3")
elif numero % 2 == 0:
    print(f"El numero {numero} es divisble entre 2")
elif numero % 3 == 0:
    print(f"El numero {numero} es divisible entre 3")
else:
    print(f"El numero {numero} no es divisble entre 2 o entre 3")