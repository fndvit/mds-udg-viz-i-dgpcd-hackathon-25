import pandas as pd
from sodapy import Socrata
import requests
import json

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

def obtain_catastro_info_single_row(row: pd.Series) -> pd.DataFrame|None:
    """
    Obtains cadastral information for a single row of data.
    Parameters:
    row (pd.Series): A pandas Series object containing at least the 'referencia_cadastral' field.
    Returns:
    pd.DataFrame: A DataFrame containing the cadastral information if the request is successful.
                  Returns None if the 'referencia_cadastral' is NaN or if the request fails.
    """
    ref = row['referencia_cadastral']
    if pd.isna(ref):
        return None
    url = f"https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?RefCat={ref}" 
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()
    else:
        print(f"Error {response.status_code}: No se pudo obtener la información")
        return None
        
    return datos