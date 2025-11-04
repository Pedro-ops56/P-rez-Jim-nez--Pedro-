nombre = "Mario ALonso"
cadena2 = "Hola a todos, mi nombre es " + nombre + " y estoy aprendiendo Python."
cadena3 = " Hola mundo"
cadena4 = "Python es genial"
cadena5 = "Aprendiendo Python es divertido y emocionante"

print(len(nombre)) # Imprime la longitud de la cadena nombre

print(nombre.upper()) # Imprime la cadena nombre en mayusculas

print(nombre.lower()) # Imprime la cadena nombre en minusculas

print(cadena2.capitalize()) # convierte el primer caracter en mayuscula y el resto a minusculas

print(cadena2.title()) # convierte la primera letra de cada palabra en mayuscula

print(cadena3)
print(cadena3.strip()) # elimina los espacios en blanco al inicio y al final de la cadena

cadenaNueva = cadena4 + 5
print(cadenaNueva) # Contenacion de cadenas

cadenaMultiplicada = cadena4 * 5
print(cadenaMultiplicada) # Multiplicacion de cadenas

print(cadena4.replace("genial", "increible")) # Reemplaza una subcadena por otra