import json
import requests
import pandas as pd
import base64

df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [25, 90, 22],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
})

csv_file = "datos.csv"
df.to_csv(csv_file, index=False)

GITHUB_USER = "alexmichalec98"
REPO_NAME = "Hackathon25"
TOKEN = "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"
FILE_PATH = "datos.csv"
URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FILE_PATH}"

with open(FILE_PATH, "rb") as f:
    content = base64.b64encode(f.read()).decode()

headers = {"Authorization": f"token {TOKEN}"}
response = requests.get(URL, headers=headers)

if response.status_code == 200: 
    sha = response.json().get("sha", "")
else: 
    sha = ""

data = {
    "message": "Actualizar datos CSV",
    "content": content,
    "sha": sha,  
}
response = requests.put(URL, headers=headers, json=data)

if response.status_code in [200, 201]:
    print(f"Archivo CSV subido correctamente a: https://{GITHUB_USER}.github.io/{REPO_NAME}/{FILE_PATH}")
else:
    print(f"Error al subir el archivo: {response.json()}")