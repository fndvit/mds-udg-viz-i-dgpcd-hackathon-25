import pandas as pd
from sodapy import Socrata
import requests

def include_año_construccion(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds the construction year ('año_construccion') to the DataFrame based on the 'referencia_cadastral' column.
    Args:
        df (pd.DataFrame): DataFrame containing a 'referencia_cadastral' column with cadastral references.
    Returns:
        pd.DataFrame: DataFrame with an additional 'any_construccio' column containing the construction year.
    
    """
    for i, referencia_catastral in enumerate(df['referencia_cadastral']):
        url = f"https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?RefCat={referencia_catastral}"
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            try:
                año_construccion = datos['consulta_dnprcResult']['bico']['bi']['debi']['ant']
                print(año_construccion)
                df.loc[i, 'año_construccion'] = año_construccion
            except KeyError:
                df.loc[i, 'año_construccion'] = pd.NA
                continue
        else:
            print(f"Error {response.status_code}: No se pudo obtener la información")
            continue
    
    return df
