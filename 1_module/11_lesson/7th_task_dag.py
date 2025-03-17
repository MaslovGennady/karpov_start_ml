"""
Test documentation
"""
from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from textwrap import dedent

with DAG(
        'hw_g-maslov_7',
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='hw_g-maslov_7',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False
) as dag:
    def print_value(ts, run_id, task_number, **kwargs):
        print(f'task number is: {task_number}')
        print(ts)
        print(run_id)

    task_doc = dedent(
        '''
        # Task Documentation
        `code`
        **bold**
        *italic *
        '''
    )

    prev_task = None
    for i in range(0, 30):
        if i < 10:
            t = BashOperator(
                task_id=f'print_task_num_{i}',
                env = {"NUMBER": str(i)},
                bash_command="echo $NUMBER",
            )
        else:
            t = PythonOperator(
                task_id=f'print_task_info_{i}',
                python_callable=print_value,
                op_kwargs={'task_number': i}
            )
        t.doc_md = task_doc
        if prev_task is not None:
            prev_task >> t
        prev_task = t
