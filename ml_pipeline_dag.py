from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def start_learning():
    from train_model import main
    main()

@dag('ml_pipeline',
          start_date=datetime(2024, 1, 1),
          schedule_interval='@daily'
          )

def ml_pipeline():
    @task.bash
    def pull_dvc():
        return 'dvc pull'

    @task.bash
    def load_data():
        return 'python dataloader'



ml_pipeline()

