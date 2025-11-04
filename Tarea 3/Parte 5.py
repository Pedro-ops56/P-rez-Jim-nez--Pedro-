# Haz un programa que pida una edad, y dependiendo del rango, muestre una categoría: Menor de 13 años -> "Niño", 13 a 17 años -> "Adolescente", 18 a 64 años -> "Adulto", 65 o más -> "Adulto mayor"
edad = int(input("Ingrese su edad: "))
if edad < 13:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")
print(f"Has ingresado una edad de: {edad} años")    