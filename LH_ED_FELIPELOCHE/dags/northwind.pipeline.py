from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'northwind_pipeline',
    default_args=default_args,
    description='Pipeline Northwind ETL',
    schedule_interval='@daily',
    catchup=False
)

# Tried using environment variables here but ended up with fixed paths
# todo: Refactor to use environment variables
extract_postgres = BashOperator(
    task_id='extract_postgres',
    bash_command='''
    cd /opt/airflow/meltano-extractor && \
    meltano elt tap-postgres target-jsonl \
    --job_id=postgres-extract-{{ ds }} \
    --state-id=postgres-state
    ''',
    dag=dag
)

extract_csv = BashOperator(
    task_id='extract_csv',
    bash_command='''
    cd /opt/airflow/meltano-extractor && \
    meltano elt tap-csv target-jsonl \
    --job_id=csv-extract-{{ ds }} \
    --state-id=csv-state
    ''',
    dag=dag
)

load_warehouse = BashOperator(
    task_id='load_warehouse',
    bash_command='''
    cd /opt/airflow/meltano-extractor && \
    meltano elt tap-jsonl target-postgres \
    --job_id=load-warehouse-{{ ds }}
    ''',
    dag=dag
)

[extract_postgres, extract_csv] >> load_warehouse