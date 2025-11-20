usuario_correcto = "admin"
contraseña_correcta = "1234"
print("Por favor, inicia sesión.")
nombre_usuario = input("Introduce tu usuario: ")
contraseña = input("Introduce tu contraseña: ")
if nombre_usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("\n¡Has iniciado sesión correctamente!")
    print(f"Bienvenido, {usuario_correcto}.")
elif nombre_usuario != usuario_correcto:
    print("\nEl usuario es incorrecto.")
else:
    print("\nLa contraseña es incorrecta.")