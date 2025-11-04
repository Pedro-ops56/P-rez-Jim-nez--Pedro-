# Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división, que se repita hasta que el usuario elija salir.

opcion = 0

while opcion != 5:
    print("calculadora basica:")
    print("1. suma")
    print("2. resta")
    print("3. multiplicación")
    print("4. division")
    print("5. salir")

    opcion = int(input("Elige una opcion: "))

    if opcion >= 1 and opcion <= 4:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))

        if opcion == 1:
            print("Resultado: ", num1 + num2)
        elif opcion == 2:
            print("Resultado: ", num1 - num2)
        elif opcion == 3:
            print("Resultado: ", num1 * num2)
        elif opcion == 4:
            if num2 != 0:
                print("Resultado: ", num1 / num2)
            else:
                print("Error: No se puede dividir entre cero.")
    elif opcion == 5:
        print("Saliendo de la calculadora...")
    else:
        print("Opción no valida. Intenta de nuevo.")