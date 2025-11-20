n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
if n1 > n2:
    print(f"El número mayor es: {n1}")
elif n2 > n1:
    print(f"No es compatible con el programa.")
else:
    print("Ambos números son iguales:", n1)