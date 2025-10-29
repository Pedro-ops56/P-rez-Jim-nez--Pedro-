# Haz un programa que pida al usuario ingresar un nombre y una edad, verifica si la persona ingresada tiene la edad suficiente para votar (Tomando en cuenta que se puede votar a partir de los 18 años), si puede votar imprime un mensaje indicando que se puede votar, en caso de que no se pueda, imprime un mensaje indicando que no se puede votar y los años que le faltan para llegar poder votar.

nombre = input("Ingrese el nombre de la persona")
edadpersona = int(input("Ingrese la edad de la persona"))

if edadpersona >= 18:
    print(f"{nombre}, tienes la edad para votar")
else:
    años_faltantes = 18 - edadpersona
    print(f"{nombre} no puedes votar. te faltan {años_faltantes} años")