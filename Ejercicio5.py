radio = float(input("Ingrese el radio de un círculo: "))
diametro = 2 * radio
pi = 3.1416
longitud_circunferencia = pi * diametro
area_circulo = pi * radio ** 2
volumen_esfera = (4/3) * pi * radio ** 3
print(f"Diámetro: {diametro}ud")
print(f"Longitud de la circunferencia: {longitud_circunferencia}ud")
print(f"Área del círculo: {area_circulo}ud^2")
print(f"Volumen de la esfera: {volumen_esfera}ud^3")