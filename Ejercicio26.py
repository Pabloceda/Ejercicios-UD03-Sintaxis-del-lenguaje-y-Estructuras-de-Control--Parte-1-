def casino():
    print(" --- Programa de Casino --- ")
    try:
        primer_dado = int(input("Introduce el primer dado: "))
        segundo_dado = int(input("Introduce el segundo dado: "))
        tercer_dado = int(input("Introduce el tercer dado: "))
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
        return
    seis_count = 0
    if primer_dado == 6:
        seis_count += 1
    if segundo_dado == 6:
        seis_count += 1
    if tercer_dado == 6:
        seis_count += 1

    match seis_count:
        case 3:
            print("Excelente")
        case 2:
            print("Muy bien")
        case 1:
            print("Regular")
        case 0:
            print("Pésimo")

casino()

