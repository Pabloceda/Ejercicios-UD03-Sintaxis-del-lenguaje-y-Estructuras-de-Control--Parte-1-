numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "Indefinida ()división entre cero"
print("El resultado de la suma entre", numero1, "y ", numero2, "es:", suma)
print("El resultado de la resta entre", numero1, "y ", numero2, "es:", resta)
print("El resultado de la multiplicación entre", numero1, "y ", numero2, "es:", multiplicacion)
print("El resultado de la división entre", numero1, "y ", numero2, "es:", division)

