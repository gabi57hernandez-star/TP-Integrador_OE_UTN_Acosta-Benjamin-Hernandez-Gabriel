def mostrar_bienvenida():
    #Muestra el encabezado inicial del sistema y la palabra clave de cancelación.

    print("=" * 50)
    print("🍔 COMEDOR UTN - SISTEMA DE PEDIDOS")
    print("=" * 50)
    print("¡Hola! Bienvenido. Te ayudo a realizar tu compra.")
    print('Escribí "CANCELAR" en cualquier momento para salir.')
    print("-" * 50)


def mostrar_menu_productos(productos):
    #Muestra el menú de productos disponibles leído desde Excel.

    print("\n📋 MENÚ DISPONIBLE:")
    print("-" * 40)
    for prod in productos:
        if prod["stock"] > 0:
            # Producto con stock: muestra precio y disponibilidad.
            print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']} ({prod['stock']} disp.)")
        else:
            # Producto sin stock: marca como no disponible.
            print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']} ❌ SIN STOCK")
    print("-" * 40)


def mostrar_zonas(zonas):
    #Muestra las zonas de entrega registradas en la base de datos.
    print("\n🚚 ZONAS DE ENTREGA:")
    for z in zonas:
        if z["entrega"] == "SI":
            print(f"  • {z['nombre']}: ✅ Delivery ({z['tiempo']})")
        else:
            print(f"  • {z['nombre']}: ❌ Solo retiro en local")

def mostrar_despedida():
    #Muestra mensaje de cierre al finalizar la conversación.
    print("\n🤖 Bot: ¡Gracias por visitarnos! 👋")