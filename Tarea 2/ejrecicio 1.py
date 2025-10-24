# Haz un programa que pida tres calificaciones y calcule su promedio con dos decimales

calificacion1 = int(input("Ingresa la primera calificacion"))
calificacion2 = int(input("Ingresa la segunda calificacion"))
calificacion3 = int(input("Ingresa la tercera calificacion"))
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

round = (promedio, 2)

print(f"el promedio es, {promedio}")