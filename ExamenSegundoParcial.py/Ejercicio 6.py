# Pide al usuario ingresar 10 productos y almacenalos en una lista. Luego muestra la lista ordenada alfabeticamente.
productos = []
for _ in range(10):
    producto = input("Ingrese un producto: ")
    productos.append(producto)
productos.sort()
print("Lista de productos ordenada alfabeticamente:")
for producto in productos:
    print(producto)