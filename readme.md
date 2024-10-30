# Control de Consumo Energético

Este proyecto consta de dos scripts en Python, `Excel1.py` y `Excel2.py`, que generan y procesan un archivo de Excel para el seguimiento del consumo y costo energético mensual, permitiendo calcular variaciones y generar un control automatizado. La automatización de esta tarea es ideal para quienes desean analizar y gestionar datos de consumo energético a lo largo de un año.

## Descripción de los Scripts

### Excel1.py

El primer script (`Excel1.py`) crea una plantilla de Excel con los meses del año y columnas para registrar el tipo de consumo, la cantidad consumida, el costo y algunos cálculos adicionales, como el costo por unidad de energía y las variaciones mensuales en el consumo y el costo. El archivo generado se guarda como `Control_de_Consumo_Energético.xlsx` en la ruta especificada, dejando preparado un formato inicial para agregar y analizar datos mensuales de consumo.

### Excel2.py

El segundo script (`Excel2.py`) carga el archivo generado por `Excel1.py` y aplica fórmulas para realizar cálculos automáticos:

- **Costo por Unidad ($/unidad):** Calcula el costo por cada unidad de energía consumida (kWh o m³), con una fórmula que evita errores de división entre cero.
- **Variación de Consumo (%) y Variación de Costo (%):** Calcula la variación porcentual en el consumo y el costo de cada mes en comparación con el mes anterior, también evitando errores en los cálculos.
- **Formato de Encabezados:** Los encabezados se resaltan en negrita para mejorar la visualización y organización de los datos en el archivo.

El archivo procesado y con las fórmulas se guarda como `Control_de_Consumo_Energético_Listo.xlsx`.

## Ejemplo de Uso

1. **Ejecutar `Excel1.py`:** Este script generará un archivo de Excel con los campos necesarios para ingresar datos mensuales de consumo y costo.
2. **Ejecutar `Excel2.py`:** Este script aplicará las fórmulas automáticas para calcular el costo por unidad de energía, así como las variaciones en el consumo y el costo. Esto permitirá tener una visión más clara de los patrones de consumo a lo largo del año.

## **Utilidad en Ingeniería de Datos**

**Este código es sumamente útil en la ingeniería de datos, ya que automatiza la creación y el procesamiento de datos en formato Excel, un paso crucial en tareas de ETL (Extracción, Transformación y Carga). La automatización de fórmulas y cálculos permite a los Data Engineers estructurar y preparar grandes volúmenes de datos de consumo energético para su posterior análisis y visualización. Además, el formato final de Excel facilita la integración de estos datos en flujos de trabajo más amplios, como la generación de reportes, la carga en bases de datos y el análisis predictivo.**

## Consideraciones

- **Ruta del Archivo:** Es importante ajustar las rutas de guardado según la estructura de carpetas de tu sistema.
- **Librerías Necesarias:** Asegúrate de tener instaladas las librerías `pandas` y `openpyxl` para que los scripts funcionen correctamente. Puedes instalarlas ejecutando:
  ```bash
  pip install pandas openpyxl
  ```
- **Compatibilidad de Versión:** Este código está diseñado para versiones de Python compatibles con `pandas` y `openpyxl`. 

## Licencia

Este proyecto está disponible para su uso y modificación según las necesidades del usuario.

