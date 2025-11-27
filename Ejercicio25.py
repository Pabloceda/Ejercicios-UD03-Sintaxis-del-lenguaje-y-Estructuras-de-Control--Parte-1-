def matricula_universidad():
    print(" --- Programa de Cálculo de la matricula de la Universidad ---")

    try:
        nombre_postulante = input("Introduce tu nombre: ")
    except ValueError:
        print("Error: Por favor, introduce un nombre válido.")
        return
    #Pedir facultad, solo son validas: Ingenieria de sistemas, derecho, ingenieria naviera, ingenieria pesquera, contabilidad y administracion  
    
    facultad_validas = ['ingenieria de sistemas', 'derecho', 'ingenieria naviera', 'ingenieria pesquera', 'contabilidad', 'administracion']
    try:
        facultad = input("Introduce la facultad: ").lower()
    except ValueError:
        print("Error: Por favor, introduce una facultad válida.")
        return
    if facultad not in facultad_validas:
        print("Error: Por favor, introduce una facultad válida.")
        return
    match facultad:
        case 'ingenieria de sistemas':
            matricula = 350
            mensualidad = 650
        case 'derecho':
            matricula = 300
            mensualidad = 550
        case 'ingenieria naviera':
            matricula = 300
            mensualidad = 500
        case 'ingenieria pesquera':
            matricula = 310
            mensualidad = 460
        case 'contabilidad':
            matricula = 280
            mensualidad = 490
        case 'administracion':
            matricula = 360
            mensualidad = 520
        case _:
            # Este caso ya está cubierto por la validación anterior, pero es buena práctica
            print("Error: Facultad no reconocida.")
            return
    
    #Mostrar el importe matricula, mensualidad, el igv 18% del total y el importe total

    igv = (matricula + mensualidad) * 0.18
    total = matricula + mensualidad + igv
    print(f"\nImporte matricula: {matricula:.2f} €")
    print(f"Importe mensualidad: {mensualidad:.2f} €")
    print(f"IGV: {igv:.2f} €")
    print(f"Importe total: {total:.2f} €")

matricula_universidad()


    
    
    
 
