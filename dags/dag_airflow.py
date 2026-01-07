from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


# Définition du DAG
with DAG(
  dag_id='dag_tbm_api_ingestion',
  description='Ingestion des données TBM depuis l\'API publique',
  start_date=datetime(2025, 1, 1),
  schedule="0 * * * *",
  catchup=False,
  tags=["tbm", "api"],
) as dag:

    #Tâche pour exécuter le script Python
    fetch_tbm_data = BashOperator(
        task_id='fetch_tbm_data',
        bash_command='python3 /opt/airflow/big-data/script/getApi.py',
    )
    
    fetch_tbm_data

    