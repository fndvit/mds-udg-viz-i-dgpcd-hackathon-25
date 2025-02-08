import pandas as pd
import urllib.request, json
import sys
import os
with urllib.request.urlopen("http://analisi.transparenciacatalunya.cat/resource/tp8v-a58g.json?$limit=1500") as url:
    postal_code_json = json.load(url)

postal_code = pd.DataFrame(postal_code_json)
postal_code['codi_postal'] = postal_code["codi_postal"].astype(str)

df = pd.read_csv('src/dades/font/data_rent.csv', low_memory=False, sep=",", dtype="str")

sys.stderr.writelines([os.getcwd()])
#df = pd.read_csv('src/dades/font/certificats.csv')

def energy_rating_to_middle(letter):
    rating_map = {
        'A': 12, 'B': 38, 'C': 63, 'D': 88,
        'E': 113, 'F': 138, 'G': 163  # Estimated middle for G
    }
    return None if letter is None else rating_map.get(str(letter).upper(), None)

df['energy_middle'] = df['qualificaci_energia'].apply(energy_rating_to_middle)
df['codi_postal_parsed'] = df["codi_postal"].astype('Int64').astype(str).str.zfill(5)
join_df = df.merge(postal_code, left_on=['codi_postal_parsed'], right_on=['codi_postal'])
result_df = join_df.groupby(['codi_municipi'], as_index=False)['energy_middle'].mean()
result_df.to_json(sys.stdout, orient='records')