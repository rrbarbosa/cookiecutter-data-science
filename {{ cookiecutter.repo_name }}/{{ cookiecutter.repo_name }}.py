"""
Basic pipeline DAG

You need to copy this file to $AIRFLOW_HOME/dags
"""

# TODO: automate the copy to the dags folder

from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'rafael',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 29),
    'email': ['rafael@3dhubs.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('dag', default_args=default_args)

# t1, t2 and t3 are examples of tasks created by instatiating operators
requirements = BashOperator(
    task_id='requirements',
    bash_command='pip install -r requirements.txt',
    dag=dag)

data = BashOperator(
    task_id='data',
    bash_command='python src/make_dataset.py',
    dag=dag)

clean = BashOperator(
    task_id='clean',
    bash_command='find . -name "*.pyc" -exec rm {} \;',
    dag=dag)

lint = BashOperator(
    task_id='flake8',
    bash_command='flake8 .',
    dag=dag)

data.set_upstream(requirements)
