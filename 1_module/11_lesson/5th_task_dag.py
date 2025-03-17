"""
Test documentation
"""
from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from textwrap import dedent

with DAG(
        'hw_g-maslov_5',
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='hw_g-maslov_5',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False
) as dag:
    template_command = dedent(
        """
        {% for i in range(5) %}
        echo "{{ ts }}"
        echo "{{ run_id }}"
        {% endfor %}
        """
    )

    bash_task = BashOperator(
        task_id = "bash_python_templated",
        bash_command = template_command,
    )
