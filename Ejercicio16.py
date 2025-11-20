numero = float(input("Introduce un número: "))
if numero < 0:
    print("Numero no valido para el programa.")
elif numero < 999:
    print("El numero tiene 3 dígitos.")
elif numero < 9999:
    print("El numero tiene 4 dígitos.")
else:
    print("El numero no es valido para el programa.")