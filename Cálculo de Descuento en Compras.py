def calcular_descuento(monto_total, descuento=10):
    """
    Calcula el descuento y retorna el valor del descuento y el monto final.
    monto_total: valor total de la compra
    descuento: porcentaje de descuento (por defecto 10%)
    """
    valor_descuento = monto_total * (descuento / 100)
    monto_final = monto_total - valor_descuento
    return valor_descuento, monto_final


# Llamadas de prueba
# Primera llamada (descuento por defecto 10%)
monto1 = 100
desc1, final1 = calcular_descuento(monto1)
print("------ PRIMERA COMPRA ------")
print(f"Monto total: ${monto1}")
print("Descuento aplicado: 10%")
print(f"Valor del descuento: ${desc1}")
print(f"Monto final a pagar: ${final1}\n")

# Segunda llamada (descuento personalizado 15%)
monto2 = 250
desc2, final2 = calcular_descuento(monto2, 15)
print("------ SEGUNDA COMPRA ------")
print(f"Monto total: ${monto2}")
print("Descuento aplicado: 15%")
print(f"Valor del descuento: ${desc2}")
print(f"Monto final a pagar: ${final2}")