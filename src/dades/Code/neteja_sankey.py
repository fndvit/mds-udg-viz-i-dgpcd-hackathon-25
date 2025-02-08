import pandas as pd

# Definimos el nombre del fichero CSV
csv_file = "total.csv"

# 1) Cargamos el fichero CSV (ajusta el separador y la codificación si fuese necesario)
df = pd.read_csv(csv_file, sep=",", encoding="utf-8")

# 2) Convertimos la columna "data_entrada" a tipo fecha (formato día/mes/año).
#    El parámetro errors="coerce" transformará en NaT las cadenas que no se puedan parsear como fecha.
df["data_entrada"] = pd.to_datetime(df["data_entrada"], dayfirst=True, errors="coerce")

# 3) Intentamos convertir la columna "Total" a float. Las celdas que no se puedan convertir
#    se marcarán como NaN. Luego descartamos filas con NaN en "Total".
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")
df = df.dropna(subset=["Total"])

# 4) Filtramos el DataFrame para quedarnos únicamente con las filas donde
#    "Indicadores de renta media y mediana" sea "Renta neta media por persona"
df_filtrado = df[df["Indicadores de renta media y mediana"] == "Renta neta media por persona"]

# 5) Ordenamos el DataFrame filtrado por la columna de fecha de entrada (data_entrada)
df_filtrado = df_filtrado.sort_values(by="data_entrada")

# 6) De cada grupo definido por 'mundissec', cogemos la última fila
#    (la más reciente según "data_entrada")
df_ultimo = df_filtrado.groupby("mundissec", as_index=False).tail(1)

# 7) Seleccionamos las columnas requeridas:
#    "Indicadores de renta media y mediana", "Total", "qualificaci_energia",
#    "mundissec" y "data_entrada" (por si queremos revisar fechas).
resultado = df_ultimo[[
    "Indicadores de renta media y mediana",
    "Total",
    "qualificaci_energia",
    "mundissec",
    "data_entrada"
]]

# 8) Visualizamos el resultado
print(resultado)
