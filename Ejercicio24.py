#Programa Tienda Don Pepe

def compras_donpepe ():
    print(" --- Cálculo de Compras en Tienda Don Pepe --- ")
    
    #Valor de la compra
    try:
        valor_compra = float(input("Introduce el valor total de la compra (€): "))
    except ValueError:
        print("Error: Por favor, introduce un número válido para el valor de la compra.")
        return
    #Día de la semana de la compra
    dia_semana = input("Introduce el día de la semana de la compra: ").strip().lower()
    dias_descuento = ['martes', 'jueves']
    if dia_semana not in ['lunes', 'martes', 'miércoles', 'miercoles', 'jueves', 'viernes', 'sábado', 'sabado', 'domingo']:
        print("Error: Día de la semana no válido.")
        return
    
    #Cálculo del descuento
    if dia_semana in dias_descuento:
        descuento = valor_compra * 0.15
        total_a_pagar = valor_compra - descuento
        print(f"\nDescuento aplicado: {descuento:.2f} €")
        print(f"Total a pagar: {total_a_pagar:.2f} €")
    else:
        total_a_pagar = valor_compra
        print("\nNo hay descuento aplicado.")
        print(f"Total a pagar: {total_a_pagar:.2f} €")
    
compras_donpepe()
