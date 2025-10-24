# Sintasis condicionales

# if condicion:
#    instrucciones si la condicion es verdadera
# elif otra condicion:
#    instrucciones si la otra condicion es verdadera
# else:
#     instrucciones si ninguna condicion es verdadera

# Ejercicio 1: programa que pida un número y muestre si es positivo, negativo o cero
numero = float(input("ingresa un número"))

if numero > 0:
    print("Bloque if ejecutado.")
    print("El número es positivo.")
elif numero < 0:
    print("Bloque elif ejecutado.")
    print("El número es negativo.")
else:
    print("El número es cero")


print("-------------------------")

# if condicion:
#    instrucciones si la condicion es verdadera
# elif otra condicion:
#    instrucciones si la otra condicion es verdadera
# else:
#    instrucciones si ninguna condicion es veradera

# Ejerciocio 2: Programa que pida dos números y muestre cúal es mayor o si son iguales

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número e mayor.")
elif num1 < num2: # num2 > num1
    print("El segundo número es mayor.")
else:
    print("ambos número son iguales.")

print("------------------------")    

# Ejercio 3: Haz un programa que pida una calificacion del 0 al 10 y muestre si está aprobado o reprobado. Toma en cuenta una calificacion mayor a 6 como aprobatoria.

nombreAlumno = input("Ingresa el nombre del alumno: ")
calificacion = float(input("Ingrese la calificacion del alumno (0-10): "))

if calificacion >= 6:
    print(f"El alumno {nombreAlumno} esta aprobado. ")
else:
    print(f"El alumno {nombreAlumno} esta reprobado. ")

print("----------------------------------")

# Ejercicio 4: Haz un programa que pida la edad de una persona y muestre si puede votar(mayor o igual a 18 años) o no

nombre = input("ingrese el nombre de la persona: ")
edadPersona = int(input("Ingrese su edad. "))

# if condicion:
#    instrucciones si la condicion es verdadera
# elif otra condicion:
#    instrucciones si la otra condicion es verdadera
# else:
#    instrucciones si ninguna condicion es veradera

if edadPersona >= 18:
    print(f"{nombre} tiene {edadPersona} años y puede votar")
else:
    print(f"{nombre} tiene {edadPersona} años y no puede votar")