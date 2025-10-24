# Haz un programa que pida un precio y muestre el total con IVA del 16%.

precio = int(input("Ingrese el precio: "))

iva = (precio * .16)
precioiva = (precio + iva)

print(f"El precio con iva es: {precioiva}")