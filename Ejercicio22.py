# 1. Pedir los datos al usuario
print("Introduce la hora actual:")
try:
    hora = int(input("Horas (0-23): "))
    minutos = int(input("Minutos (0-59): "))
    segundos = int(input("Segundos (0-59): "))

    # Validamos que los datos sean lógicos
    if (0 <= hora <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59):
        
        # 2. Sumamos un segundo
        segundos = segundos + 1

        # 3. Comprobamos el "efecto dominó"
        if segundos == 60:
            segundos = 0          # Reiniciamos segundos
            minutos = minutos + 1 # Sumamos un minuto

            if minutos == 60:
                minutos = 0       # Reiniciamos minutos
                hora = hora + 1   # Sumamos una hora

                if hora == 24:
                    hora = 0      # Reiniciamos hora (medianoche)

        # 4. Mostramos el resultado
        # El :02d sirve para que siempre muestre dos cifras (ej: 05 en vez de 5)
        print(f"\nLa hora más un segundo es: {hora:02d}:{minutos:02d}:{segundos:02d}")

    else:
        print("\nError: La hora introducida no es válida.")

except ValueError:
    print("\nError: Debes introducir números enteros.")