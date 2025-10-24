# Haz un programa que pida el radio y la altura de un cilindro y muestre su volumen.
import math

radio = float(input("Ingresa el radio de tu cilindro: "))
altura = float(input("Ingresa la altura de tu cilindro: "))

radiocuadrado = math.pow (radio, 2)
areabase = (radiocuadrado * 3.1416)
volumen = (areabase * altura)

print(f"El volumen del cilindro es: {volumen}")