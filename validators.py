def validar_opcion_producto(entrada, productos_disponibles):
    try:
        opcion = int(entrada)
    except ValueError:
        raise ValueError("Debes ingresar un número válido.")

    if opcion <= 0:
        raise ValueError("El número debe ser mayor a 0.") 

    ids_validos = [p["id"] for p in productos_disponibles if p["stock"] > 0]
    if opcion not in ids_validos:
        raise ValueError("Ese producto no existe o no tiene stock.")

    return opcion


def validar_cantidad(entrada, stock_maximo):
    try:
        cantidad = int(entrada)
    except ValueError:
        raise ValueError("Debes ingresar un número entero válido.")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")

    if cantidad > stock_maximo:
        raise ValueError(f"Stock insuficiente. Máximo disponible: {stock_maximo}.")

    return cantidad


def validar_confirmacion(entrada):
    texto = entrada.strip().upper()
    if texto not in ["SI", "NO"]:
        raise ValueError('Debes responder SI o NO.')
    return texto


def validar_zona(entrada, zonas):
    texto = entrada.strip().upper()
    zonas_nombres = [z["nombre"].upper() for z in zonas]
    if texto not in zonas_nombres:
        raise ValueError("Esa zona no está registrada. Consultá las zonas disponibles.")
    return texto


def validar_nombre(entrada):
    nombre = entrada.strip()
    if len(nombre) < 2:
        raise ValueError("El nombre debe tener al menos 2 caracteres.")
    return nombre


def validar_telefono(entrada):
    telefono = entrada.strip()
    if not telefono.isdigit() or len(telefono) < 7:
        raise ValueError("Ingresá un teléfono válido (solo números, mínimo 7 dígitos).")
    return telefono


def validar_direccion(entrada):
    direccion = entrada.strip()
    if len(direccion) < 5:
        raise ValueError("La dirección debe tener al menos 5 caracteres.")
    return direccion
