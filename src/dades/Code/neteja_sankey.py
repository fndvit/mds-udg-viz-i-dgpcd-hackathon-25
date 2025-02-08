import pandas as pd
import numpy as np

# 1) Cargamos el fichero CSV (ajusta el separador y la codificación si fuese necesario)
df = pd.read_csv("total.csv", sep=",", encoding="utf-8")

# 2) Convertimos la columna "data_entrada" a tipo fecha.
df["data_entrada"] = pd.to_datetime(df["data_entrada"], dayfirst=True, errors="coerce")

# 3) Intentamos convertir la columna "Total_Rent_2022" a float.
#    Las celdas que no se puedan convertir se marcan como NaN y luego se eliminan.
df["Total_Rent_2022"] = pd.to_numeric(df["Total_Rent_2022"], errors="coerce")
df = df.dropna(subset=["Total_Rent_2022"])

# 4) Calculamos la mediana global del "Total_Rent_2022"
mediana_global = df["Total_Rent_2022"].median()

# 5) Filtramos filas donde "Indicadores de renta media y mediana" sea "Renta neta media por persona"
df_filtrado = df[df["Indicadores de renta media y mediana"] == "Renta neta media por persona"]
df_filtrado = df_filtrado.sort_values(by="data_entrada")

# 6) De cada 'mundissec' tomamos la última fila (la de fecha más reciente)
df_ultimo = df_filtrado.groupby("mundissec", as_index=False).tail(1)

# 7) Añadimos una columna "clase" en función de la comparación con la mediana global
conditions = [
    df_ultimo["Total_Rent_2022"] < 0.75 * mediana_global,
    (df_ultimo["Total_Rent_2022"] >= 0.75 * mediana_global) & (df_ultimo["Total_Rent_2022"] <= 2.0 * mediana_global),
    df_ultimo["Total_Rent_2022"] > 2.0 * mediana_global
]
choices = ["Clase baja", "Clase media", "Clase alta"]

# CORRECCIÓN: Agregar `default="Desconocido"` para evitar el error de tipos
df_ultimo["clase"] = np.select(conditions, choices, default="Desconocido")

# 8) Seleccionamos las columnas requeridas
resultado = df_ultimo[[
    "Indicadores de renta media y mediana",
    "Total_Rent_2022",
    "qualificaci_energia",
    "rehabilitacio_energetica",
    "mundissec",
    "data_entrada",
    "clase"
]]

# 9) Crear un nuevo DataFrame con las columnas solicitadas
resumen = resultado.groupby(["clase", "rehabilitacio_energetica", "qualificaci_energia"]).size().reset_index(name="counts")

# 10) Guardar el resultado en un archivo CSV
resumen.to_csv("resultado.csv", index=False, encoding="utf-8")

# 11) Imprimimos el resultado para verificar
print(resultado)
