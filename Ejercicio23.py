def compras_farmacia():
    print(" --- Cálculo de Compras en Farmacia --- ")
    
    try:
        valor_compra = float(input("Introduce el valor total de la compra (€): "))
    except ValueError:
        print("Error: Por favor, introduce un número válido para el valor de la compra.")
        return
    
    metodo_pago = input("Introduce el método de pago (contado/tarjeta): ").strip().lower()
    if metodo_pago not in ['contado', 'tarjeta']:
        print("Error: Método de pago no válido. Usa 'contado' o 'tarjeta'.")
        return
    
    if metodo_pago == 'contado':
        descuento = valor_compra * 0.05
        total_a_pagar = valor_compra - descuento
        print(f"\nDescuento aplicado: {descuento:.2f} €")
    else:  
        recargo = valor_compra * 0.03
        total_a_pagar = valor_compra + recargo
        print(f"\nRecargo aplicado: {recargo:.2f} €")
    
    print(f"Total a pagar: {total_a_pagar:.2f} €")
    
compras_farmacia()
