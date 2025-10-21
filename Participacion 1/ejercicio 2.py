# Haz un programa que solicite al usuario la base y la altura de un rectangulo y calcula su area y perimetro

base = int(input("Ingresa la base del rectangulo"))
altura = int(input("Ingresa la altura del rectangulo"))

area = (base * altura)
perimetro = ((base + altura) * 2)

print(f'el ara del rectangulo es: {area}.')
print(f'el perimetro del rectangulo es: {perimetro}.')