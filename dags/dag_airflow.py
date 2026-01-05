# from airflow import DAG
# from airflow.operators.bash import BashOperator
# from datetime import datetime, timedelta

# default_args = {
#     'owner': 'Axel',
#     'depends_on_past': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# #Définition du DAG
# with DAG(
#   dag_id='dag_tbm_api_ingestion',
#   description='Ingestion des données TBM depuis l\'API publique',
#   default_args=default_args,
#   start_date=datetime(2026, 1, 5),
#   schedule_interval='@hourly',
#   catchup=False,
#   tags=['tbm', 'api', 'hdfs', 'etl'],
# ) as dag:
  
#     #Tâche pour exécuter le script Python
#     fetch_tbm_data = BashOperator(
#         task_id='fetch_tbm_data',
#         bash_command='python3 /path/to/your/script/getApi.py',
#     )

#     fetch_tbm_data = BatchOperator(
#       task_id='getApi',
#       batch_command=()
#         "cd /home/axel/Documents/workspace-nexa/big-data/script/"
#         "&& python3 getApi.py"
#       ),
#     )