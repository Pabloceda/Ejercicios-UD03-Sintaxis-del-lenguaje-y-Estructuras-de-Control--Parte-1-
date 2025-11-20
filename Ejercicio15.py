a = int(input("Introduce el primer número (a): "))
b = int(input("Introduce el segundo número (b): "))
c = int(input("Introduce el tercer número (c): "))

    # 2. Comprobar los casos
    
    # Caso 1: Los tres son iguales
if a == b and b == c:
        print(f"Los tres números son iguales: {a}")

    # Caso 2: Solo 'a' y 'b' son iguales
elif a == b:
        if a > c:
            print(f"Mayores (iguales): {a} y {b}")
            print(f"Menor: {c}")
        else: # c > a
            print(f"Mayor: {c}")
            print(f"Menores (iguales): {a} y {b}")
    
    # Caso 3: Solo 'a' y 'c' son iguales
elif a == c:
        if a > b:
            print(f"Mayores (iguales): {a} y {c}")
            print(f"Menor: {b}")
        else: # b > a
            print(f"Mayor: {b}")
            print(f"Menores (iguales): {a} y {c}")
            
    # Caso 4: Solo 'b' y 'c' son iguales
elif b == c:
        if b > a:
            print(f"Mayores (iguales): {b} y {c}")
            print(f"Menor: {a}")
        else: # a > b
            print(f"Mayor: {a}")
            print(f"Menores (iguales): {b} y {c}")

    # Caso 5: Todos son diferentes
else:
        print("Los tres números son diferentes.")
        # Encontramos el mayor
        if a > b and a > c:
            print(f"El mayor es: {a}")
        elif b > a and b > c:
            print(f"El mayor es: {b}")
        else:
            print(f"El mayor es: {c}")
            
        # Encontramos el menor
        if a < b and a < c:
            print(f"El menor es: {a}")
        elif b < a and b < c:
            print(f"El menor es: {b}")
        else:
            print(f"El menor es: {c}")