import sys
from bot_engine import ejecutar_conversacion
from display import mostrar_bienvenida
from data_manager import inicializar_base_de_datos


def main():
    try:
        # Genera el archivo Excel con datos iniciales,si no existe.
        # Esto evita perder pedidos guardados entre ejecuciones.
        inicializar_base_de_datos()

        #Muestra mensaje de bienvenida y instrucciones iniciales
        mostrar_bienvenida()

        #Inicia conversacion con la máquina de estados
        ejecutar_conversacion()

    # Captura Ctrl+C para interrumpir el flujo si el usuario lo elige
    except KeyboardInterrupt:
        print("\n\n🚫 Conversación interrumpida.")
        sys.exit(0)
    ## Captura cualquier error inesperado
    except Exception as e:
        print(f"\n❌ Error inesperado en la aplicación: {e}")
        sys.exit(1)

#Main se ejecuta solo si se llama directamente al archivo
if __name__ == "__main__":
    main()
