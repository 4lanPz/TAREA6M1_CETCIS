# =====================================================
# Problema 3: Navegación para Vehículo Autónomo

# Leer datos de sensores de proximidad y cámara
def leer_sensores():
    frente = float(input("Distancia al frente (metros): "))
    izquierda = float(input("Distancia a la izquierda (metros): "))
    derecha = float(input("Distancia a la derecha (metros): "))

    print("\nEstado de la cámara:")
    print("1. Camino despejado")
    print("2. Obstáculo detectado")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        camara = "camino despejado"
    else:
        camara = "obstáculo detectado"

    return {
        "frente": frente,
        "izquierda": izquierda,
        "derecha": derecha,
        "camara": camara
    }

# Procedimiento para calcular la ruta óptima
def calcular_ruta(origen, destino):
    ruta = ["Inicio", "Avenida Principal", "Calle 5", "Destino"]
    print("Ruta calculada:", ruta)

# Función para detectar y evitar obstáculos
def detectar_y_evitar_obstaculo(distancia):
    if distancia < 2:
        return "Obstáculo detectado: frenar o cambiar de dirección"
    else:
        return "Camino libre"

# Procedimiento para ajustar la velocidad según el tráfico
def ajustar_velocidad(trafico):
    if trafico == "alto":
        print("Velocidad recomendada: 30 km/h")
    elif trafico == "medio":
        print("Velocidad recomendada: 45 km/h")
    else:
        print("Velocidad recomendada: 60 km/h")


print("=== Sistema de Navegación ===")

sensores = leer_sensores()

print("\nDatos de sensores:")
for direccion, dato in sensores.items():
    if direccion != "camara":
        print(direccion, ":", dato, "metros")
        print(detectar_y_evitar_obstaculo(dato))

print("Cámara:", sensores["camara"])

# Datos quemados para simplificar
calcular_ruta("Inicio", "Destino")
ajustar_velocidad("alto")
