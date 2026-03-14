# =====================================================
# Problema 5: Sistema de Riego Automatizado

# Leer sensores de humedad
def leer_humedad():
    zonas = {}

    print("Ingrese la humedad del suelo para cada zona:")

    zonas["zona1"] = float(input("Humedad zona1 (%): "))
    zonas["zona2"] = float(input("Humedad zona2 (%): "))
    zonas["zona3"] = float(input("Humedad zona3 (%): "))

    return zonas


# Consultar previsión meteorológica
def consultar_clima():
    print("\nEstado del clima:")
    print("1. Sin lluvia")
    print("2. Lluvia")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 2:
        return "lluvia"
    else:
        return "sin_lluvia"


# Calcular cantidad óptima de riego
def calcular_riego(humedad, clima):
    if clima == "lluvia":
        return 0
    elif humedad < 35:
        return 20
    elif humedad < 50:
        return 10
    else:
        return 0


# Controlar válvulas de riego
def controlar_valvula(zona, agua):
    if agua > 0:
        print(f"Regando {zona} con {agua} litros")
    else:
        print(f"{zona} no necesita riego")


print("=== Sistema de Riego Automatizado ===")

humedad = leer_humedad()
clima = consultar_clima()

print("\nClima actual:", clima)
print("\nDecisiones de riego:")

for zona, nivel in humedad.items():
    agua = calcular_riego(nivel, clima)
    controlar_valvula(zona, agua)