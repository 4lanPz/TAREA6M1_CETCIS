# =====================================================
# Problema 4: Optimización de Producción en una Fábrica

# Función para monitorear el estado de las máquinas
def monitorear_maquinas():
    return {
        "maquina1": "operativa",
        "maquina2": "mantenimiento",
        "maquina3": "operativa"
    }

# Procedimiento para planificar el mantenimiento preventivo
def planificar_mantenimiento(maquinas):
    for maquina, estado in maquinas.items():
        if estado == "mantenimiento":
            print(f"Programar revisión preventiva para {maquina}")

# Función para analizar el rendimiento de la producción
def analizar_rendimiento(unidades, horas):
    if horas > 0:
        return unidades / horas
    return 0

# Procedimiento para ajustar la programación según la demanda
def ajustar_produccion(demanda):
    if demanda > 100:
        print("Aumentar producción")
    else:
        print("Mantener producción normal")


print("=== Sistema de Optimización de Producción ===")

# Obtener datos de las máquinas
maquinas = monitorear_maquinas()

print("\nEstado de las máquinas:")
for maquina, estado in maquinas.items():
    print(f"{maquina}: {estado}")

# Revisar mantenimiento
print("\nRevisión de mantenimiento:")
planificar_mantenimiento(maquinas)

# Datos de producción
unidades = int(input("Ingrese las unidades producidas: "))
horas = int(input("Ingrese las horas trabajadas: "))
demanda = int(input("Ingrese la demanda actual: "))

# Calcular rendimiento
rendimiento = analizar_rendimiento(unidades, horas)
print("\nRendimiento de producción:", rendimiento)

# Ajustar producción según demanda
print("\nAjuste de producción:")
ajustar_produccion(demanda)
