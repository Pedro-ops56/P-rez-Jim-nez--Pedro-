# Haz un programa que genera la tabla de multiplicar de un número ingresado. Al final, muestra cuantos resultados de las multiplicaciones fueron mayores que 50, cuántos menores que 50 y cuántos iguales a 50.

numero = int(input("Ingrese un numero para crear su tabla de multiplicar"))
contador_mayoresde50 = 0
contador_menoresde50 = 0
contador_igualesde50 = 0
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    if resultado >50:
        contador_mayoresde50 += 1
    elif resultado <50:
        contador_menoresde50 += 1
    else:
        contador_igualesde50 += 1
print(f"Los numeros mayores a 50 son: {contador_mayoresde50}")
print(f"Los numeros menores a 50 son: {contador_menoresde50}")
print(f"Los numeros iguales a 50 son: {contador_igualesde50}")