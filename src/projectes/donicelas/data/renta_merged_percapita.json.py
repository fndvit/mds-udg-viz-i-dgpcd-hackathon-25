import pandas as pd
import urllib.request, json
import sys
import os


sys.stderr.writelines([os.getcwd()])

data = pd.read_csv('src/dades/font/data_rent.csv', low_memory=False, sep=",", dtype="str")

cens = pd.read_csv('src/dades/font/cens2023.csv', low_memory=False, sep=";", dtype="str")


# Filtrar el cens segons la teva condició anterior
cens = cens.loc[(cens["edat"] == "total") & (cens["sexe"] == "total")].reset_index()

# Convertir ambdues columnes a string abans de fer el merge
data['codi_poblacio'] = data['codi_poblacio'].astype(str)
cens["geo"] = cens["geo"].astype(str)

# Ajustar la columna "geo" per eliminar l'última xifra
cens["geo"] = cens["geo"].str.slice(0, -1)

# Unir les dues taules segons "codi_poblacio" de data_cens i "geo" de cens
data_cens = data.merge(cens[["geo", "valor"]], left_on="codi_poblacio", right_on="geo", how="left").reset_index(drop=True).reset_index()

# Canviar el nom de la columna "valor" a "cens"
data_cens = data_cens.rename(columns={"valor": "cens"})

# Guardar la taula "data_cens" com a fitxer CSV
data_cens.to_csv("data_cens.csv", index=False)

# Eliminar espais en blanc extres i convertir a numèric
data_cens["Puntuacion_Energetica"] = pd.to_numeric(data_cens["Puntuacion_Energetica"].astype(str).str.strip(), errors="coerce")
data_cens["Renta ultimo año"] = pd.to_numeric(data_cens["Renta ultimo año"].astype(str).str.strip(), errors="coerce")

# Agrupar per municipi i calcular les mitjanes i la moda
data_plot3 = data_cens.groupby("codi_poblacio").agg(
    poblacio=("poblacio", lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]),
    cens=("cens", lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]),
    qualificacio=("Puntuacion_Energetica", "mean"),
    renta=("Renta ultimo año", "mean")
).reset_index()

# Arrodonir a un decimal
data_plot3["qualificacio"] = data_plot3["qualificacio"].round(1)
data_plot3["renta"] = data_plot3["renta"].round(1)

# Eliminar les files on NaN
data_plot3 = data_plot3.dropna().reset_index()

# Eliminar municipis amb menys de 5000 habitants
data_plot3["cens"] = data_plot3["cens"].astype('int64')
data_plot3 = data_plot3.loc[data_plot3["cens"] >= 2000].reset_index()

# Guardar la taula "data_plot3" com a fitxer CSV




data_plot3.to_json(sys.stdout, orient='records')