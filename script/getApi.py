import requests
from datetime import datetime
import json
import os
import sys

class VelibAPI:
    url = "https://datahub.bordeaux-metropole.fr/explore/dataset/ci_vcub_p/download/?format=json&timezone=Europe/Paris&lang=fr"
    
    def fetch_and_save(self):
        # 1. CHEMIN ABSOLU : On pointe vers le volume monté dans Docker
        # Votre docker-compose monte le projet dans /opt/airflow/big-data
        folder = "/opt/airflow/big-data/data/raw/"
        
        # 2. CRÉATION DU DOSSIER : On s'assure que le dossier existe avant d'écrire
        if not os.path.exists(folder):
            print(f"Le dossier {folder} n'existe pas, création en cours...")
            os.makedirs(folder)

        try:
            response = requests.get(self.url)
            response.raise_for_status() # Lève une erreur si l'API répond 404 ou 500
            
            now = datetime.now()
            fileName = f"tbm_{now.strftime('%Y-%m-%d_%Hh%M')}.json"
            full_path = os.path.join(folder, fileName)
            
            with open(full_path, "w") as output_file:
                data = response.json()
                json.dump(data, output_file, indent=4)
                
            print(f"Fichier créé : {full_path}")
            
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier : {e}")
            # 3. SIGNAL D'ERREUR : Indispensable pour qu'Airflow marque la tache en ROUGE (Failed)
            sys.exit(1)

if __name__ == "__main__":
    VelibAPI().fetch_and_save()