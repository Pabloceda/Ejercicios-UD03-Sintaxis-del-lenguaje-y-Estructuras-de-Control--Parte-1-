try:
    nota = float(input("Introduce la calificación (0-10): "))
    match nota:
        case n if n < 0 or n > 10:
            print("Error: La nota debe estar entre 0 y 10.")
            
        case n if 0 <= n < 3:
            print("Muy Deficiente")
            
        case n if 3 <= n < 5:
            print("Insuficiente")

        case n if 5 <= n < 6:
            print("Suficiente")

        case n if 6 <= n < 7:
            print("Bien")
            
        case n if 7 <= n < 9:
            print("Notable")
            
        case n if 9 <= n <= 10:
            print("Sobresaliente")
            
        case _: 
            print("Valor no reconocido")

except ValueError:
    print("Error: Debes introducir un número.")
