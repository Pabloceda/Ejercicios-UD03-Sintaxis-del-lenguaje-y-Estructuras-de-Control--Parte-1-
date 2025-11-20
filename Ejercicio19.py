# 1. Definimos el saldo inicial fuera del bucle
saldo = 1000

print("Bienvenido a su Cajero Virtual")

# 2. Iniciamos el bucle infinito para el menú
while True:
    print("\n" + "-"*30) # Línea decorativa
    print("MENÚ DE OPCIONES:")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    print("-"*30)

    try:
        # Solicitamos la opción
        opcion = int(input("Elija una opción (1-3): "))

        if opcion == 1:
            # --- OPCIÓN 1: INGRESAR ---
            ingreso = float(input("¿Cuánto dinero desea ingresar?: "))
            if ingreso > 0:
                saldo += ingreso # Sumamos al saldo (saldo = saldo + ingreso)
                print(f"¡Dinero ingresado! Su saldo actual es: ${saldo}")
            else:
                print("Error: La cantidad a ingresar debe ser positiva.")

        elif opcion == 2:
            # --- OPCIÓN 2: RETIRAR ---
            retiro = float(input("¿Cuánto dinero desea retirar?: "))
            
            # Comprobaciones de seguridad:
            if retiro > saldo:
                print(f"Error: No tiene saldo suficiente. Su saldo es: ${saldo}")
            elif retiro <= 0:
                print("Error: La cantidad a retirar debe ser mayor que 0.")
            else:
                saldo -= retiro # Restamos al saldo (saldo = saldo - retiro)
                print(f"¡Retiro exitoso! Su saldo actual es: ${saldo}")

        elif opcion == 3:
            # --- OPCIÓN 3: SALIR ---
            print("Gracias por utilizar nuestro cajero automático. ¡Hasta pronto!")
            break # 'break' rompe el bucle while y termina el programa

        else:
            # --- OPCIÓN NO VÁLIDA (ej. 4, 5, -1) ---
            print("Opción incorrecta. Por favor, elija 1, 2 o 3.")

    except ValueError:
        # Esto captura si el usuario escribe letras en lugar de números en el menú
        print("Error: Por favor, introduzca un número válido.")



