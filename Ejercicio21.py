def calcular_nomina():
    print("--- CALCULADORA DE SALARIO NETO SEMANAL ---")
    
    # 1. ENTRADA DE DATOS
    nombre = input("Introduce el nombre del trabajador: ")
    try:
        horas_trabajadas = float(input("Introduce las horas trabajadas esta semana: "))
        tarifa_hora = float(input("Introduce la tarifa por hora (€): "))
    except ValueError:
        print("Error: Por favor, introduce números válidos para horas y tarifa.")
        return

    # 2. CÁLCULO DEL SALARIO BRUTO (Lógica de horas extra)
    # Las primeras 35 horas son normales, el resto se pagan x1.5
    
    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * tarifa_hora
    else:
        # Calculamos las horas normales y las extras
        horas_extras = horas_trabajadas - 35
        salario_bruto = (35 * tarifa_hora) + (horas_extras * tarifa_hora * 1.5)

    # 3. CÁLCULO DE IMPUESTOS (Tasas progresivas)
    # Tramo 1: 0 - 500€   -> 0%
    # Tramo 2: 501 - 900€ -> 25%
    # Tramo 3: > 900€     -> 45%
    
    impuestos = 0.0
    
    if salario_bruto <= 500:
        impuestos = 0.0
        
    elif salario_bruto <= 900:
        # Solo paga impuestos por la cantidad que supera los 500
        base_imponible = salario_bruto - 500
        impuestos = base_imponible * 0.25
        
    else: # Si gana más de 900 euros
        # 1. Los primeros 500 son gratis.
        # 2. Los siguientes 400 (de 500 a 900) pagan el 25%.
        impuesto_tramo_2 = 400 * 0.25  # Esto son 100€ fijos
        
        # 3. El resto (lo que pasa de 900) paga el 45%
        resto = salario_bruto - 900
        impuesto_tramo_3 = resto * 0.45
        
        impuestos = impuesto_tramo_2 + impuesto_tramo_3

    # 4. CÁLCULO DEL SALARIO NETO
    salario_neto = salario_bruto - impuestos

    # 5. SALIDA DE RESULTADOS
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

# Ejecutamos la función
calcular_nomina()