# ==========================================
# Problema 2: Gestión de Inventario en un Almacén

inventario = {
    "teclados": 20,
    "ratones": 35,
    "monitores": 10
}

productos = list(inventario.keys())

# Registrar entrada
def registrar_entrada(producto, cantidad):
    inventario[producto] += cantidad

# Registrar salida
def registrar_salida(producto, cantidad):
    if inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
    else:
        print("No hay suficiente cantidad")

# Nivel óptimo
def nivel_optimo(producto):
    return 15

# Alertas
def alerta_reabastecimiento(producto):
    if inventario[producto] < nivel_optimo(producto):
        print(f"ALERTA: reabastecer {producto}")

print("=== Sistema de Gestión de Inventarios ===")

print("\nInventario actual:")
for i, producto in enumerate(productos, start=1):
    print(f"{i}. {producto}: {inventario[producto]}")

# Elegir producto por número
opcion = int(input("\nSeleccione el número del producto: "))
producto = productos[opcion - 1]

cantidad = int(input("Ingrese la cantidad: "))
movimiento = input("Tipo de movimiento (entrada/salida): ")

if movimiento == "entrada":
    registrar_entrada(producto, cantidad)
elif movimiento == "salida":
    registrar_salida(producto, cantidad)

print("\nInventario actualizado:")
for producto, cantidad in inventario.items():
    print(f"{producto}: {cantidad}")
    alerta_reabastecimiento(producto)
