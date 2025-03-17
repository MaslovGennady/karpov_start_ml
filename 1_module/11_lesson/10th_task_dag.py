"""
Test documentation
"""
from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from textwrap import dedent

with DAG(
        'hw_g-maslov_10',
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='hw_g-maslov_10',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False
) as dag:
    def push_for_operator(ti):
        return 'Airflow tracks everything'

    def pull_for_operator(ti):
        res = ti.xcom_pull(
            key='return_value',
            task_ids = 'push_task'
        )
        print(res)

    push_task = PythonOperator(
        task_id=f'push_task',
        python_callable=push_for_operator
    )

    pull_task = PythonOperator(
        task_id=f'pull_task',
        python_callable=pull_for_operator
    )
       
    push_task >> pull_task
