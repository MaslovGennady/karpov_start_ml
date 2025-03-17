"""
Test documentation
"""
from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

from textwrap import dedent
from psycopg2.extras import DictCursor


with DAG(
        'hw_g-maslov_11',
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='hw_g-maslov_11',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False
) as dag:

    def get_active_user():
        postgres = PostgresHook(postgres_conn_id='startml_feed')
        with postgres.get_conn() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                query = '''
                    select user_id, count(1) as "count"
                    from feed_action
                    where action = 'like'
                    group by user_id 
                    order by count(1) desc 
                    limit 1
                '''
                cursor.execute(query)
                result = cursor.fetchone()
        return {'user_id': result[0], 'count': result[1]}


    task = PythonOperator(
        task_id=f'task',
        python_callable=get_active_user
    )
