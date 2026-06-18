# TP-Integrador_OE_UTN_Acosta-Benjamin-Hernandez-Gabriel

## Sistema de Toma de Pedidos - Comedor UTN

### Contexto de Negocio

El proceso manual de toma de pedidos (llamadas telefónicas, anotaciones en papel, cálculo manual de precios y verificación visual de stock) genera errores de transcripción, pérdida de información y demoras operativas. Este sistema automatiza el flujo completo mediante un bot conversacional que valida datos, gestiona zonas de entrega y persiste la información en tiempo real.

### Requisitos

- Python 3.8+
- openpyxl

### Con terminal bash:

#### 1. Clonar el repositorio

```bash
git clone https://github.com/gabi57hernandez-star/TP-Integrador_OE_UTN_Acosta-Benjamin-Hernandez-Gabriel
cd TP-Integrador_OE_UTN_Acosta-Benjamin-Hernandez-Gabriel
```

#### 2. Instalar dependencias

```bash
pip install openpyxl
```

#### 3. Ejecutar la aplicación

```bash
python main.py
```

> **Nota:** Al primer run, el sistema genera automáticamente el archivo `comedor_db.xlsx` con los datos iniciales (productos, zonas y estructura de pedidos). Si el archivo ya existe, no se sobrescribe para preservar los pedidos guardados.

### Documentación del Proyecto

La documentación completa (diagramas BPMN, diccionario de datos, manual de usuario, pruebas de estrés y evidencia de herramientas de IA) se encuentra en el informe técnico en formato PDF.

### Autores

- Gabriel Hernández
- Benjamín Acosta

*Comisión 11 / Comisión 4 - Tecnicatura Universitaria en Programación a Distancia - UTN*