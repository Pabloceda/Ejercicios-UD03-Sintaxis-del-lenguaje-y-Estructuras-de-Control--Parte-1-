# 1. Pedir los datos al usuario
print("Introduce la hora actual:")
try:
    hora = int(input("Horas (0-23): "))
    minutos = int(input("Minutos (0-59): "))
    segundos = int(input("Segundos (0-59): "))

    if (0 <= hora <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59):
        
        segundos = segundos + 1

        if segundos == 60:
            segundos = 0          
            minutos = minutos + 1 

        if minutos == 60:
            minutos = 0       
            hora = hora + 1   

        if hora == 24:
            hora = 0      

        print(f"\nLa hora más un segundo es: {hora:02d}:{minutos:02d}:{segundos:02d}")

    else:
        print("\nError: La hora introducida no es válida.")

except ValueError:
    print("\nError: Debes introducir números enteros.")