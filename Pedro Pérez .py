# Programa que pida un nùmero entero positivo y muestre su raiz cuadrada, raiz cubica
# potencia al cuadrado y potencia al cubo

import math

numero = int(input("ingresa un numero entero positivo"))

raizCuadrada = math.sqrt(numero)
raizCubica = numero ** (1/3)
potenciaCuadrado = pow(numero, 2)
potenciaCubica = pow(numero, 3)

print(f'La raiz cudarda de {numero} es: {raizCuadrada}.')
print(f'La raiz cubica de {numero} es: {raizCubica}.')
print(f'La potencia al cuadrado de {numero} es: {potenciaCuadrado}.')
print(f'La potecencia al cubo es {numero} es: {potenciaCubica}.')