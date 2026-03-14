# ==========================================
# Problema 1: Control de Temperatura en un Edificio Inteligente

# Leer datos manualmente
def leer_datos_sensores():
    zonas = []

    cantidad = int(input("Ingrese el número de zonas: "))

    for i in range(cantidad):
        print(f"\nZona {i+1}")

        nombre = input("Nombre de la zona: ")
        temperatura_actual = float(input("Temperatura actual: "))
        temperatura_externa = float(input("Temperatura externa: "))
        hora = int(input("Hora del día: "))

        ocupada_input = input("¿La zona está ocupada? (si/no): ")
        ocupada = ocupada_input.lower() == "si"

        zona = {
            "nombre": nombre,
            "temperatura_actual": temperatura_actual,
            "ocupada": ocupada,
            "temperatura_externa": temperatura_externa,
            "hora": hora
        }

        zonas.append(zona)

    return zonas

# Función para calcular la temperatura óptima
def calcular_temperatura_optima(hora, ocupada, temperatura_externa):

    temperatura_optima = 22

    if not ocupada:
        temperatura_optima = 24

    if hora >= 18 or hora < 6:
        temperatura_optima += 1

    if temperatura_externa > 30:
        temperatura_optima -= 1
    elif temperatura_externa < 15:
        temperatura_optima += 1

    return temperatura_optima


# Procedimiento para enviar señal al sistema
def enviar_ajuste(zona, temperatura_actual, temperatura_optima):

    print(f"\nZona: {zona}")
    print(f"Temperatura actual: {temperatura_actual}°C")
    print(f"Temperatura óptima: {temperatura_optima}°C")

    if temperatura_actual > temperatura_optima:
        print("Acción: Activar refrigeración")
    elif temperatura_actual < temperatura_optima:
        print("Acción: Activar calefacción")
    else:
        print("Acción: Mantener temperatura actual")


# Función para registrar consumo
def registrar_consumo(temperatura_actual, temperatura_optima):
    diferencia = abs(temperatura_actual - temperatura_optima)
    consumo = diferencia * 1.5
    return consumo


print("=== Sistema de Control de Temperatura ===")

zonas = leer_datos_sensores()
consumo_total = 0

for zona in zonas:
    nombre = zona["nombre"]
    temp_actual = zona["temperatura_actual"]
    ocupada = zona["ocupada"]
    temp_externa = zona["temperatura_externa"]
    hora = zona["hora"]

    temp_optima = calcular_temperatura_optima(hora, ocupada, temp_externa)
    enviar_ajuste(nombre, temp_actual, temp_optima)

    consumo = registrar_consumo(temp_actual, temp_optima)
    consumo_total += consumo

    print(f"Consumo estimado en {nombre}: {consumo} W")

print("\n=== Resumen ===")
print(f"Consumo total estimado: {consumo_total} W")