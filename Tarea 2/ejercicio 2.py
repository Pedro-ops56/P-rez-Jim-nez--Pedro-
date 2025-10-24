# Haz un programa que calcule el area de un circulo a partir de su radio
import math

radio = float(input("Ingresa el radio de tu circulo"))

potencia = math.pow (radio, 2)

area = (potencia * 3.1416)

print(f"El area del circulo es: {area}")