a = int(input("Introduce el primer número (a): "))
b = int(input("Introduce el segundo número (b): "))
c = int(input("Introduce el tercer número (c): "))
    
if a == b and b == c:
    print(f"Los tres números son iguales: {a}")
elif a == b:
    if a > c:
        print(f"Mayores (iguales): {a} y {b}")
        print(f"Menor: {c}")
    else:
        print(f"Mayor: {c}")
        print(f"Menores (iguales): {a} y {b}")
elif a == c:
    if a > b:
        print(f"Mayores (iguales): {a} y {c}")
        print(f"Menor: {b}")
    else:
        print(f"Mayor: {b}")
        print(f"Menores (iguales): {a} y {c}")
elif b == c:
    if b > a:
        print(f"Mayores (iguales): {b} y {c}")
        print(f"Menor: {a}")
    else:
        print(f"Mayor: {a}")
        print(f"Menores (iguales): {b} y {c}")
else:
    print("Los tres números son diferentes.")
    if a > b and a > c:
        print(f"El mayor es: {a}")
    elif b > a and b > c:
        print(f"El mayor es: {b}")
    else:
        print(f"El mayor es: {c}")
    if a < b and a < c:
        print(f"El menor es: {a}")
    elif b < a and b < c:
        print(f"El menor es: {b}")
    else:
        print(f"El menor es: {c}")