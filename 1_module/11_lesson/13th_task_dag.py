"""
Test documentation
"""
from datetime import datetime, timedelta
from airflow import DAG

from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator


with DAG(
        'hw_g-maslov_13',
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='hw_g-maslov_13',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False
) as dag:
    def get_variable():
        if Variable.get('is_startml') == 'True':
            return "startml_desc"
        return 'not_startml_desc'

    branch_task = BranchPythonOperator(
        task_id='branch_task',
        python_callable=get_variable,
    )

    def startml_print():
        print("StartML is a starter course for ambitious people")

    startml_task = PythonOperator(
        task_id='startml_desc',
        python_callable=startml_print,
    )

    def not_startml_print():
        print("Not a startML course, sorry")

    not_startml_task = PythonOperator(
        task_id='not_startml_desc',
        python_callable=not_startml_print,
    )

    start_task = EmptyOperator(task_id='empty_start_task')
    finish_task = EmptyOperator(task_id='empty_finish_task')

    start_task >> branch_task >> [startml_task, not_startml_task] >> finish_task
