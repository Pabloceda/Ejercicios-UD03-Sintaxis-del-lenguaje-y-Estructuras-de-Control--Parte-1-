precio_articulo = float(input("Ingrese el precio del artículo: "))
precio_venta_real = float(input("Ingrese el precio de venta real del artículo: "))

porcentaje_residual = (precio_articulo * 100) / precio_venta_real
porcentaje_descuento = 100 - porcentaje_residual

print(f"El descuento es del: {porcentaje_descuento}%")