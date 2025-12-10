# Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.
contraseña = input("Ingrese una contraseña: ")

def es_contraseña_valida(contraseña):
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    return len(contraseña) >= 8 and tiene_mayuscula and tiene_numero

if es_contraseña_valida(contraseña):
    print("Contraseña válida")
else:
    print("Contraseña inválida")
# --- IGNORE ---