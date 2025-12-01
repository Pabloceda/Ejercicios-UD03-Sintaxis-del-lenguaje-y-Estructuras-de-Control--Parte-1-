def calcular_nomina():
    print("--- CALCULADORA DE SALARIO NETO SEMANAL ---")
    
    nombre = input("Introduce el nombre del trabajador: ")
    try:
        horas_trabajadas = float(input("Introduce las horas trabajadas esta semana: "))
        tarifa_hora = float(input("Introduce la tarifa por hora (€): "))
    except ValueError:
        print("Error: Por favor, introduce números válidos para horas y tarifa.")
        return

    
    
    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * tarifa_hora
    else:
        horas_extras = horas_trabajadas - 35
        salario_bruto = (35 * tarifa_hora) + (horas_extras * tarifa_hora * 1.5)

    impuestos = 0.0
    
    if salario_bruto <= 500:
        impuestos = 0.0
        
    elif salario_bruto <= 900:
        base_imponible = salario_bruto - 500
        impuestos = base_imponible * 0.25
        
    else: 
        impuesto_tramo_2 = 400 * 0.25  
        
        resto = salario_bruto - 900
        impuesto_tramo_3 = resto * 0.45
        
        impuestos = impuesto_tramo_2 + impuesto_tramo_3

    salario_neto = salario_bruto - impuestos

    print("\n" + "="*30)
    print(f"RECIBO DE NÓMINA: {nombre.upper()}")
    print("="*30)
    print(f"Horas trabajadas: {horas_trabajadas} h")
    print(f"Tarifa por hora:  {tarifa_hora} €/h")
    print("-" * 30)
    print(f"Salario Bruto:    {salario_bruto:.2f} €")
    print(f"Tasas (Impuestos): -{impuestos:.2f} €")
    print("-" * 30)
    print(f"SALARIO NETO:     {salario_neto:.2f} €")
    print("="*30)

calcular_nomina()