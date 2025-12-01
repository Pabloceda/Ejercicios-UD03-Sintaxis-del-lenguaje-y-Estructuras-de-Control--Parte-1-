saldo = 1000

print("Bienvenido a su Cajero Virtual")
while True:
    print("\n" + "-"*30) 
    print("MENÚ DE OPCIONES:")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    print("-"*30)

    try:
        opcion = int(input("Elija una opción (1-3): "))

        if opcion == 1:
            ingreso = float(input("¿Cuánto dinero desea ingresar?: "))
            if ingreso > 0:
                saldo += ingreso 
                print(f"¡Dinero ingresado! Su saldo actual es: ${saldo}")
            else:
                print("Error: La cantidad a ingresar debe ser positiva.")

        elif opcion == 2:
            retiro = float(input("¿Cuánto dinero desea retirar?: "))
            
            if retiro > saldo:
                print(f"Error: No tiene saldo suficiente. Su saldo es: ${saldo}")
            elif retiro <= 0:
                print("Error: La cantidad a retirar debe ser mayor que 0.")
            else:
                saldo -= retiro 
                print(f"¡Retiro exitoso! Su saldo actual es: ${saldo}")

        elif opcion == 3:
            print("Gracias por utilizar nuestro cajero automático. ¡Hasta pronto!")
            break 

        else:
            print("Opción incorrecta. Por favor, elija 1, 2 o 3.")

    except ValueError:
        print("Error: Por favor, introduzca un número válido.")



