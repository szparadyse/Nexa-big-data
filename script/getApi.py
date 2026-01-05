
import requests
from datetime import datetime
import json



url = "https://datahub.bordeaux-metropole.fr/explore/dataset/ci_vcub_p/download/?format=json&timezone=Europe/Paris&lang=fr"
response = requests.get(url)
now = datetime.now()
fileName = f"tbm_{now.strftime('%Y-%m-%d_%Hh%M')}.json"
folder = "data/raw/"
try:
    with open(folder + fileName, "w") as output_file:
        data = response.json()  # On transforme la réponse en dictionnaire
        json.dump(data, output_file, indent=4) # On écrit le JSON formaté
    print(f"Fichier créé : {folder + fileName}")
except Exception as e:
    print(f"Erreur lors de la sauvegarde du fichier : {e}")
  