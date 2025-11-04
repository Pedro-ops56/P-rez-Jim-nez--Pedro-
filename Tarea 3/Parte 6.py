# Haz un programa que pida un número, y muestre si es primo o no.
numero = int(input("Ingrese un numero: "))
primo = True
if numero <= 1:
    primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            
if primo:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")
print(f"Has ingresado el numero: {numero}")