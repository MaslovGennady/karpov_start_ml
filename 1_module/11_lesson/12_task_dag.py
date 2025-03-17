"""
Test documentation
"""
from datetime import datetime, timedelta
from airflow import DAG

from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


with DAG(
        'hw_g-maslov_12',
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='hw_g-maslov_12',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False
) as dag:

    def get_variable():
        print(Variable.get("is_startml"))

    task = PythonOperator(
        task_id=f'task',
        python_callable=get_variable
    )
