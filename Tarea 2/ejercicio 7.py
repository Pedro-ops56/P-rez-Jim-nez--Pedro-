# Haz un programa que pida un número y muestre si está entre 10 y 20 (solo mostrando True o False).

# if condicion:
#    instrucciones si la condicion es verdadera
# elif otra condicion:
#    instrucciones si la otra condicion es verdadera
# else:
#     instrucciones si ninguna condicion es verdadera

numero = int(input("Ingrese un numero"))

if numero < 20:
    print("Bloque if ejecutado")
    print("true")
else:
    print("false")