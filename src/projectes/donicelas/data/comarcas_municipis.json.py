from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import sys
import geopandas as gpd
import json
import tempfile

sys.stderr.writelines(["Initiating"])
tmpDirectory = tempfile.mkdtemp()
catalunya_zip_url = 'https://datacloud.icgc.cat/datacloud/divisions-administratives/shp/divisions-administratives-v2r1-20240705.zip'
file_response_by_request = urlopen(catalunya_zip_url)
zip_file_memory = ZipFile(BytesIO(file_response_by_request.read()))
sys.stderr.writelines(["Read"])

# The ZIP file contains multiple shapefiles at different levels or scales. A scale map of 1:1,000,000 is sufficient.
files_shape_selected = [file_name for file_name in zip_file_memory.namelist() if 'comarques-1000000' in file_name]
for level_map_file in files_shape_selected:
    with zip_file_memory.open(level_map_file) as file:
        with open(f'{tmpDirectory}/{level_map_file}', 'wb') as f:
            f.write(file.read())

sys.stderr.writelines(["Comparques"])
comarques_df = gpd.read_file(
    f"{tmpDirectory}/{next(file_name for file_name in files_shape_selected if file_name.endswith('.shp'))}")
sys.stderr.writelines([str(len(comarques_df.geometry))])

sys.stderr.writelines(["Geometry Comarques"])
# Change to CRS 4326 - d3 standard
comarques_df = comarques_df.to_crs(epsg=4326)
sys.stderr.writelines([str(len(comarques_df.geometry))])

sys.stderr.writelines(["comarques df"])


# The ZIP file contains multiple shapefiles at different levels or scales. A scale map of 1:1,000,000 is sufficient.
files_shape_selected = [file_name for file_name in zip_file_memory.namelist() if 'municipis-1000000' in file_name]
for level_map_file in files_shape_selected:
    with zip_file_memory.open(level_map_file) as file:
        with open(f'{tmpDirectory}/{level_map_file}', 'wb') as f:
            f.write(file.read())

sys.stderr.writelines(["municipis"])

municipis_df = gpd.read_file(
    f"{tmpDirectory}/{next(file_name for file_name in files_shape_selected if file_name.endswith('.shp'))}")
sys.stderr.writelines([str(len(municipis_df.geometry))])

sys.stderr.writelines(["municipis df"])

# Change to CRS 4326 - d3 standard
municipis_df = municipis_df.to_crs(epsg=4326)
sys.stderr.writelines([str(len(municipis_df.geometry))])

sys.stderr.writelines(["municipis df ASD"])


comarques_json = json.loads(comarques_df.to_json())
municipis_json = json.loads(municipis_df.to_json())

cm = {
   'comarques': comarques_json,
   'municipis': municipis_json,
}
json.dump(cm, fp=sys.stdout)
