def mostrar_bienvenida():
    print("=" * 50)
    print("🍔 COMEDOR UTN - SISTEMA DE PEDIDOS")
    print("=" * 50)
    print("¡Hola! Bienvenido. Te ayudo a realizar tu compra.")
    print('Escribí "CANCELAR" en cualquier momento para salir.')
    print("-" * 50)


def mostrar_menu_productos(productos):
    print("\n📋 MENÚ DISPONIBLE:")
    print("-" * 40)
    for prod in productos:
        if prod["stock"] > 0:
            print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']} ({prod['stock']} disp.)")
        else:
            print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']} ❌ SIN STOCK")
    print("-" * 40)


def mostrar_zonas(zonas):
    print("\n🚚 ZONAS DE ENTREGA:")
    for z in zonas:
        if z["entrega"] == "SI":
            print(f"  • {z['nombre']}: ✅ Delivery ({z['tiempo']})")
        else:
            print(f"  • {z['nombre']}: ❌ Solo retiro en local")


def mostrar_despedida():
    print("\n🤖 Bot: ¡Gracias por visitarnos! 👋")
