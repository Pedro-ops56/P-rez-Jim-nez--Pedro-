# En python existen los siguientes modos de lectura y escritura de archivos:
# 'r' - Modo de lectura (read): Abre un archivo para leer su contenido. El archivo debe existir, sino existe el programa nos marcara un error.
# 'w' - Modo de escritura (write): Abre un archivo para escribir en él. Si el archivo ya existe, se sobreescribe. Si no existe, se creará uno nuevo.
# 'a' - Modo de anexado (append): Abre un archivo para agregar contenido al final del mismo. Si el archivo no existe, se creará uno nuevo.
# 'r+' - Modo de lectura y escritura (read and write): Abre un archivo para leer y escribir en él. Si el archivo no existe, el programa marcará un error.
# 'w+' - Modo de escritura y lectura (write and read): Abre un archivo para escribir y leer en él. Si el archivo ya existe, se sobreescribe. Si no existe, se creará uno nuevo.
# 'a+' - Modo de anexado y lectura (append and read): Abre un archivo para agregar contenido al final y leerlo. Si el archivo no existe, se creará uno nuevo.

#Apertura de archivos
# open("Ruta/archivo.txt", "modo")

#Cerrar archivos
# archivo.close()

# Podemos abir el archivo haciendo uso de 'with', el cual cierra el archivo de manera automatica al finalizar el bloque de codigo.

# with open("Ruta/archivo.txt", "modo") as archivo:
     # Operaciones con el archivo


with open("archivo.txt", 'r') as f:
    contenido = f.read() # Leer todo el contenido del archivo, y lo va a almacenar en la variable del contenido
print(contenido)

with open("archivo.txt", 'r') as f:
    for linea in f: # Leer el archivo linea por linea
        print(linea.strip()) # Imprimir cada linea sin espacios adicionales

with open("archivos2.txt", 'w')as f:
    f.write("Esta es una nueva linea escrita en el archivo.\n") # Escribir una linea en el archivo
    f.write("Otra linea añadida al archivo.\n")

with open("archivos3.txt", 'a') as f:
    f.write("Esta linea se ha añadido al final del archivo.\n") # Escribir una linea al final del archivo
    
with open("archivo.txt", 'r+') as f:
    contenido = f.read() # Leer el contenido del archivo
    f.write("\nEsta linea se ha añadido al final del archivo usando r+.\n")

with open("archivos2.txt", 'w+') as f:
    f.write("Escribiendo en archivo2 usando w+.\n")
    f.seek(0) # Volver al inicio del archivo para leer lo que se escribio
    contenido = f.read()
    print(contenido)

with open("archivos3.txt", 'a+') as f:
    f.write("Anadiendo una linea usando a+.\n")
    f.seek(0) # Volver al inicio del archivo para leer todo el contenido
    contenido = f.read()
    print(contenido)