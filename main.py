import sys
from bot_engine import ejecutar_conversacion
from display import mostrar_bienvenida
from data_manager import inicializar_base_de_datos


def main():
    try:
        inicializar_base_de_datos()
        mostrar_bienvenida()
        ejecutar_conversacion()
    except KeyboardInterrupt:
        print("\n\n🚫 Conversación interrumpida.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado en la aplicación: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
