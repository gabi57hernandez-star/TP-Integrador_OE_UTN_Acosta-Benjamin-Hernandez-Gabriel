from data_manager import (
    obtener_productos,
    obtener_zonas,
    obtener_siguiente_nro_orden,
    guardar_pedido,
    actualizar_stock,
    obtener_info_zona,
)
from validators import (
    validar_opcion_producto,
    validar_cantidad,
    validar_confirmacion,
    validar_zona,
    validar_nombre,
    validar_telefono,
    validar_direccion,
)
from display import mostrar_menu_productos, mostrar_zonas, mostrar_despedida


def palabra_cancelar():
    return "CANCELAR"


def crear_estado():
    return {
        "estado": "INICIO",
        "producto": None,
        "cantidad": 0,
        "cliente": "",
        "telefono": "",
        "direccion": "",
        "zona": "",
        "total": 0,
        "nro_orden": 0,
    }


def verificar_cancelacion(entrada):
    return entrada.strip().upper() == palabra_cancelar()


def obtener_input_con_cancelacion():
    entrada = input("👤 Cliente: ")
    if verificar_cancelacion(entrada):
        print("\n🤖 Bot: Pedido cancelado. ¡Hasta luego!")
        return None, True
    return entrada, False


def procesar_estado_inicio(estado):
    productos = obtener_productos()
    mostrar_menu_productos(productos)
    print("\n🤖 Bot: Seleccioná el número del producto que querés:")
    estado["estado"] = "SELECCION"
    return productos


def procesar_seleccion_producto(estado, entrada, productos):
    try:
        opcion = validar_opcion_producto(entrada, productos)
        for p in productos:
            if p["id"] == opcion:
                estado["producto"] = p
                break
        print(f"\n🤖 Bot: Elegiste {estado['producto']['nombre']}.")
        print(f"¿Cuántas unidades querés? (Stock disponible: {estado['producto']['stock']})")
        estado["estado"] = "CANTIDAD"
    except ValueError as e:
        print(f"\n⚠️ Error: {e}")
        print("Intentá de nuevo.")


def procesar_cantidad(estado, entrada):
    try:
        cantidad = validar_cantidad(entrada, estado["producto"]["stock"])
        estado["cantidad"] = cantidad
        estado["total"] = estado["producto"]["precio"] * cantidad
        print(f"\n🤖 Bot: Perfecto. Subtotal: ${estado['total']}")
        print("¿Cómo te llamás?")
        estado["estado"] = "NOMBRE"
    except ValueError as e:
        print(f"\n⚠️ Error: {e}")
        print("Intentá de nuevo.")


def procesar_nombre(estado, entrada):
    try:
        nombre = validar_nombre(entrada)
        estado["cliente"] = nombre
        print("\n🤖 Bot: ¿Cuál es tu teléfono? (solo números)")
        estado["estado"] = "TELEFONO"
    except ValueError as e:
        print(f"\n⚠️ Error: {e}")


def procesar_telefono(estado, entrada):
    try:
        telefono = validar_telefono(entrada)
        estado["telefono"] = telefono
        zonas = obtener_zonas()
        mostrar_zonas(zonas)
        print("\n🤖 Bot: ¿En qué zona/barrio querés recibir el pedido?")
        estado["estado"] = "ZONA"
    except ValueError as e:
        print(f"\n⚠️ Error: {e}")


def procesar_zona(estado, entrada):
    try:
        zonas = obtener_zonas()
        nombre_zona = validar_zona(entrada, zonas)
        estado["zona"] = nombre_zona
        info_zona = obtener_info_zona(nombre_zona, zonas)

        if info_zona["entrega"] == "NO":
            print(f"\n⚠️ En {info_zona['nombre']} no hay delivery.")
            print("🤖 Bot: ¿Querés retirar en el local? (SI/NO)")
            estado["estado"] = "CONFIRMA_RETIRO"
        else:
            print(f"\n✅ Delivery disponible. Tiempo estimado: {info_zona['tiempo']}")
            print("🤖 Bot: ¿Cuál es tu dirección de entrega?")
            estado["estado"] = "DIRECCION"
    except ValueError as e:
        print(f"\n⚠️ Error: {e}")


def procesar_confirma_retiro(estado, entrada):
    try:
        respuesta = validar_confirmacion(entrada)
        if respuesta == "SI":
            estado["direccion"] = "Retiro en local"
            mostrar_resumen(estado)
            print("\n🤖 Bot: ¿Confirmás el pedido? (SI/NO)")
            estado["estado"] = "CONFIRMA"
        else:
            print("\n🤖 Bot: Pedido cancelado por no haber delivery en tu zona.")
            estado["estado"] = "CANCELADO"
    except ValueError as e:
        print(f"\n⚠️ Error: {e}")


def procesar_direccion(estado, entrada):
    try:
        direccion = validar_direccion(entrada)
        estado["direccion"] = direccion
        mostrar_resumen(estado)
        print("\n🤖 Bot: ¿Confirmás el pedido? (SI/NO)")
        estado["estado"] = "CONFIRMA"
    except ValueError as e:
        print(f"\n⚠️ Error: {e}")


def mostrar_resumen(estado):
    print("\n" + "=" * 50)
    print("📋 RESUMEN DE TU PEDIDO")
    print("=" * 50)
    print(f"Producto: {estado['producto']['nombre']}")
    print(f"Cantidad: {estado['cantidad']}")
    print(f"Total: ${estado['total']}")
    print(f"Cliente: {estado['cliente']}")
    print(f"Teléfono: {estado['telefono']}")
    print(f"Zona: {estado['zona']}")
    print(f"Dirección: {estado['direccion']}")
    print("=" * 50)


def procesar_confirmacion(estado, entrada):
    try:
        respuesta = validar_confirmacion(entrada)
        if respuesta == "SI":
            nro_orden = obtener_siguiente_nro_orden()
            estado["nro_orden"] = nro_orden
            actualizar_stock(estado["producto"]["id"], estado["cantidad"])
            guardar_pedido(
                nro_orden,
                estado["cliente"],
                estado["telefono"],
                estado["direccion"],
                estado["producto"]["nombre"],
                estado["cantidad"],
                estado["total"],
                "Confirmado",
                estado["zona"],
            )
            print(f"\n🎉 ¡Pedido confirmado! N° de orden: {nro_orden}")
            print(f"🤖 Bot: Gracias por tu compra, {estado['cliente']}.")
            estado["estado"] = "FIN"
        else:
            print("\n🤖 Bot: Pedido cancelado. Volvé a empezar cuando quieras.")
            estado["estado"] = "CANCELADO"
    except Exception as e:
        print(f"\n❌ Error al procesar el pedido: {e}")
        print("🤖 Bot: Por favor, contactá al administrador.")
        estado["estado"] = "ERROR"


def procesar_reinicio(entrada):
    texto = entrada.strip().upper()
    if texto == "SI":
        return crear_estado(), False
    elif texto == "NO" or verificar_cancelacion(entrada):
        mostrar_despedida()
        return None, True
    else:
        print("\n🤖 Bot: Respuesta no válida. Cerrando sesión.")
        mostrar_despedida()
        return None, True


def ejecutar_conversacion():
    estado = crear_estado()
    productos = []

    while True:
        try:
            if estado["estado"] == "INICIO":
                productos = procesar_estado_inicio(estado)

            elif estado["estado"] == "SELECCION":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_seleccion_producto(estado, entrada, productos)

            elif estado["estado"] == "CANTIDAD":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_cantidad(estado, entrada)

            elif estado["estado"] == "NOMBRE":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_nombre(estado, entrada)

            elif estado["estado"] == "TELEFONO":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_telefono(estado, entrada)

            elif estado["estado"] == "ZONA":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_zona(estado, entrada)

            elif estado["estado"] == "DIRECCION":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_direccion(estado, entrada)

            elif estado["estado"] == "CONFIRMA_RETIRO":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_confirma_retiro(estado, entrada)

            elif estado["estado"] == "CONFIRMA":
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                procesar_confirmacion(estado, entrada)

            elif estado["estado"] in ["FIN", "CANCELADO", "ERROR"]:
                print("\n🤖 Bot: ¿Querés hacer otro pedido? (SI/NO)")
                entrada, cancelado = obtener_input_con_cancelacion()
                if cancelado:
                    break
                estado, salir = procesar_reinicio(entrada)
                if salir:
                    break

        except KeyboardInterrupt:
            print("\n\n🚫 Conversación interrumpida por el usuario.")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("🤖 Bot: Se reinicia la conversación por seguridad.")
            estado = crear_estado()
