import pandas as pd

# Crear un DataFrame como plantilla para el archivo de control de consumo energético
data = {
    'Mes': ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    'Tipo de Consumo': [""] * 12,    # Columna para seleccionar electricidad o gas
    'Consumo (kWh o m³)': [None] * 12,  # Columna para ingresar el consumo mensual
    'Costo ($)': [None] * 12,       # Columna para ingresar el costo mensual
    'Costo por Unidad ($/unidad)': [None] * 12, # Columna de cálculo automático del costo por unidad de energía
    'Variación de Consumo (%)': [None] * 12,   # Columna para el cálculo de la variación porcentual en el consumo
    'Variación de Costo (%)': [None] * 12,     # Columna para el cálculo de la variación porcentual en el costo
}

# Crear el DataFrame de la hoja de control de consumo energético
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
output_path = "/data/Control_de_Consumo_Energético.xlsx"
df.to_excel(output_path, index=False)

output_path
